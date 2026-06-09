/* Cinematic product-shot prompt enhancer — uses Claude to craft an AI-image-generator-ready prompt */
exports.handler = async (event) => {
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Content-Type': 'application/json'
  };

  if (event.httpMethod === 'OPTIONS') return { statusCode: 200, headers, body: '' };
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey || !apiKey.startsWith('sk-ant-')) {
    return { statusCode: 401, headers, body: JSON.stringify({ error: 'API key not configured on server' }) };
  }

  try {
    const { beverageType, containerType, style = 'luxury' } = JSON.parse(event.body);

    if (!beverageType || !containerType) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'beverageType and containerType are required' }) };
    }

    const system = `You are a professional product photography AI prompt engineer specialising in cinematic beverage campaigns. Transform brief product shot descriptions into ultra-detailed, technically precise prompts optimised for AI image generators (DALL-E 3, Midjourney v6, Stable Diffusion XL).

Output ONLY the final prompt — no explanations, no markdown, no labels.

Requirements:
- Specific lighting (key light angle, rim light intensity, fill ratio, colour temperature in Kelvin)
- Material optics (fresnel effect, subsurface scattering, caustics, refraction index, microfacet roughness)
- Camera/lens specs (focal length in mm, f-stop, depth of field, bokeh quality)
- Professional CGI vocabulary (octane render / Arnold / Redshift, ray-traced reflections, GI, HDR environment map)
- Exact colour palette (hex-like descriptors or pantone-style names)
- Mood, atmosphere, compositional rule (rule of thirds, leading lines)
- Maximum 240 words, single flowing paragraph`;

    const userMsg = `Create a cinematic product still prompt for:
BEVERAGE: ${beverageType}
CONTAINER: ${containerType}
STYLE: ${style}

BASE BRIEF: Ultra-realistic floating 3D product shot of ${beverageType} in a ${containerType}. The liquid reflects the natural colour and texture of the drink, appearing realistic and fresh. The container is glossy with subtle condensation. The product floats midair surrounded by ingredients naturally associated with the beverage, arranged dynamically. Liquid splashes and droplets are suspended in motion, forming clean, realistic arcs that enhance a sense of freshness and energy. Background is a soft gradient that matches and complements the natural colour of the beverage and its ingredients, creating a cohesive and visually appealing palette.`;

    const res = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-haiku-4-5-20251001',
        max_tokens: 700,
        system,
        messages: [{ role: 'user', content: userMsg }]
      })
    });

    const data = await res.json();
    if (!res.ok) {
      return { statusCode: res.status, headers, body: JSON.stringify({ error: data.error?.message || 'Claude API error' }) };
    }

    const prompt = data.content?.[0]?.text?.trim() || '';

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ prompt, beverageType, containerType })
    };

  } catch (err) {
    return { statusCode: 500, headers, body: JSON.stringify({ error: err.message }) };
  }
};
