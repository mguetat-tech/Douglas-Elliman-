"""Tests pour src/post_generator.py — RED écrit en premier, puis GREEN."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from post_generator import format_price, generate_caption, render_html

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


# ── format_price ────────────────────────────────────────────────────────────

class TestFormatPrice:
    def test_millions_exact(self):
        assert format_price(2_000_000) == "2 M€"

    def test_millions_with_decimal(self):
        assert format_price(3_500_000) == "3,5 M€"

    def test_uses_french_comma_not_dot(self):
        result = format_price(1_850_000)
        assert "." not in result
        assert "," in result

    def test_one_decimal_place_max(self):
        result = format_price(2_750_000)
        assert result == "2,8 M€"

    def test_returns_euro_symbol(self):
        assert "€" in format_price(1_000_000)


# ── generate_caption ─────────────────────────────────────────────────────────

class TestGenerateCaption:
    def test_contains_property_name(self):
        caption = generate_caption(PROPERTY_FIXTURE)
        assert "Chalet Test" in caption

    def test_contains_formatted_price(self):
        caption = generate_caption(PROPERTY_FIXTURE)
        assert "3,5 M€" in caption

    def test_contains_surface(self):
        caption = generate_caption(PROPERTY_FIXTURE)
        assert "280 m²" in caption

    def test_contains_pieces(self):
        caption = generate_caption(PROPERTY_FIXTURE)
        assert "7" in caption

    def test_contains_location(self):
        caption = generate_caption(PROPERTY_FIXTURE)
        assert "Mont d'Arbois" in caption
        assert "Megève" in caption

    def test_contains_douglas_elliman_hashtag(self):
        caption = generate_caption(PROPERTY_FIXTURE)
        assert "#DouglasElliman" in caption

    def test_contains_megeve_hashtag(self):
        caption = generate_caption(PROPERTY_FIXTURE)
        assert "#Megève" in caption

    def test_contains_description(self):
        caption = generate_caption(PROPERTY_FIXTURE)
        assert "Vue Mont-Blanc" in caption


# ── render_html ──────────────────────────────────────────────────────────────

class TestRenderHtml:
    def test_replaces_nom_variable(self):
        html = render_html(PROPERTY_FIXTURE)
        assert "Chalet Test" in html
        assert "{{nom}}" not in html

    def test_replaces_price_variable(self):
        html = render_html(PROPERTY_FIXTURE)
        assert "3,5 M€" in html
        assert "{{prix_affiche}}" not in html

    def test_replaces_surface_variable(self):
        html = render_html(PROPERTY_FIXTURE)
        assert "280" in html
        assert "{{surface_m2}}" not in html

    def test_replaces_location_variable(self):
        html = render_html(PROPERTY_FIXTURE)
        assert "Mont d'Arbois" in html
        assert "{{localisation}}" not in html

    def test_no_template_variables_remaining(self):
        html = render_html(PROPERTY_FIXTURE)
        assert "{{" not in html

    def test_uses_placeholder_when_no_image(self):
        prop = {**PROPERTY_FIXTURE, "image_url": None}
        html = render_html(prop)
        assert "image-placeholder" in html
        assert "<img" not in html

    def test_uses_img_tag_when_url_provided(self):
        prop = {**PROPERTY_FIXTURE, "image_url": "https://example.com/photo.jpg"}
        html = render_html(prop)
        assert '<img src="https://example.com/photo.jpg"' in html
        # Le CSS définit toujours .image-placeholder — on vérifie l'absence de la div
        assert 'class="image-placeholder"' not in html

    def test_contains_douglas_elliman_brand(self):
        html = render_html(PROPERTY_FIXTURE)
        assert "Douglas Elliman" in html
