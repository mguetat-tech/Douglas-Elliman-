"""Tests pour src/ai_caption_generator.py — mocks API, pas d'appels réels."""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import ai_caption_generator
from ai_caption_generator import generate_ai_captions

PROPERTY_FIXTURE = {
    "id": "test-chalet-01",
    "nom": "Chalet Test",
    "prix": 3_500_000,
    "surface_m2": 280,
    "pieces": 7,
    "chambres": 5,
    "localisation": "Mont d'Arbois",
    "description": "Vue Mont-Blanc, spa privé",
    "image_url": None,
}

MOCK_CAPTIONS = {
    "sensorielle": "✦ Chalet Test ✦\n\nL'air vif du Mont-Blanc à portée de main.\n3,5 M€ · 280 m² · 7 pièces\n📍 Mont d'Arbois, Megève\n\nMessage privé ou lien en bio.\n\n#DouglasElliman #Megève #ChaletLuxe",
    "narrative": "✦ Chalet Test ✦\n\nDes matins de ski, des soirées au coin du feu.\n3,5 M€ · 280 m² · 7 pièces\n📍 Mont d'Arbois, Megève\n\nMessage privé ou lien en bio.\n\n#DouglasElliman #Megève #AlpineLuxury",
    "exclusive": "✦ Chalet Test ✦\n\nRarissime au Mont d'Arbois — dernière opportunité de ce calibre.\n3,5 M€ · 280 m² · 7 pièces\n📍 Mont d'Arbois, Megève\n\nMessage privé ou lien en bio.\n\n#DouglasElliman #Megève #LuxuryRealEstate",
}


def _mock_response(json_data: dict) -> MagicMock:
    text_block = MagicMock()
    text_block.type = "text"
    text_block.text = json.dumps(json_data)

    response = MagicMock()
    response.content = [text_block]
    return response


def _mock_response_with_thinking(json_data: dict) -> MagicMock:
    thinking_block = MagicMock()
    thinking_block.type = "thinking"
    thinking_block.thinking = "Analysing the property..."

    text_block = MagicMock()
    text_block.type = "text"
    text_block.text = json.dumps(json_data)

    response = MagicMock()
    response.content = [thinking_block, text_block]
    return response


class TestGenerateAiCaptions:
    def test_returns_three_variants(self):
        with patch.object(ai_caption_generator, "Anthropic") as MockClient:
            MockClient.return_value.messages.create.return_value = _mock_response(MOCK_CAPTIONS)
            result = generate_ai_captions(PROPERTY_FIXTURE)
        assert set(result.keys()) == {"sensorielle", "narrative", "exclusive"}

    def test_sensorielle_contains_property_name(self):
        with patch.object(ai_caption_generator, "Anthropic") as MockClient:
            MockClient.return_value.messages.create.return_value = _mock_response(MOCK_CAPTIONS)
            result = generate_ai_captions(PROPERTY_FIXTURE)
        assert "Chalet Test" in result["sensorielle"]

    def test_all_variants_contain_douglas_elliman_hashtag(self):
        with patch.object(ai_caption_generator, "Anthropic") as MockClient:
            MockClient.return_value.messages.create.return_value = _mock_response(MOCK_CAPTIONS)
            result = generate_ai_captions(PROPERTY_FIXTURE)
        for variant, caption in result.items():
            assert "#DouglasElliman" in caption, f"#{variant} manque #DouglasElliman"

    def test_uses_opus_model(self):
        with patch.object(ai_caption_generator, "Anthropic") as MockClient:
            mock_create = MockClient.return_value.messages.create
            mock_create.return_value = _mock_response(MOCK_CAPTIONS)
            generate_ai_captions(PROPERTY_FIXTURE)
        assert mock_create.call_args[1]["model"] == "claude-opus-4-7"

    def test_uses_adaptive_thinking(self):
        with patch.object(ai_caption_generator, "Anthropic") as MockClient:
            mock_create = MockClient.return_value.messages.create
            mock_create.return_value = _mock_response(MOCK_CAPTIONS)
            generate_ai_captions(PROPERTY_FIXTURE)
        assert mock_create.call_args[1]["thinking"] == {"type": "adaptive"}

    def test_system_prompt_has_cache_control(self):
        with patch.object(ai_caption_generator, "Anthropic") as MockClient:
            mock_create = MockClient.return_value.messages.create
            mock_create.return_value = _mock_response(MOCK_CAPTIONS)
            generate_ai_captions(PROPERTY_FIXTURE)
        system = mock_create.call_args[1]["system"]
        assert isinstance(system, list)
        assert system[0]["cache_control"] == {"type": "ephemeral"}

    def test_skips_thinking_blocks_in_response(self):
        with patch.object(ai_caption_generator, "Anthropic") as MockClient:
            MockClient.return_value.messages.create.return_value = _mock_response_with_thinking(MOCK_CAPTIONS)
            result = generate_ai_captions(PROPERTY_FIXTURE)
        assert set(result.keys()) == {"sensorielle", "narrative", "exclusive"}

    def test_price_formatted_in_user_message(self):
        with patch.object(ai_caption_generator, "Anthropic") as MockClient:
            mock_create = MockClient.return_value.messages.create
            mock_create.return_value = _mock_response(MOCK_CAPTIONS)
            generate_ai_captions(PROPERTY_FIXTURE)
        user_content = mock_create.call_args[1]["messages"][0]["content"]
        assert "3,5 M€" in user_content
