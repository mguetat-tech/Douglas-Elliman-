// Synchronisation contacts entre la mémoire locale et le CRM (Notion)
// Lit project_deals.md et synchronise les entrées vers une base Notion

const fs = require('fs');
const path = require('path');

const NOTION_API_KEY = process.env.NOTION_API_KEY || '';
const NOTION_DATABASE_ID = process.env.NOTION_DATABASE_ID || '';
const MEMORY_PATH = path.join(__dirname, '..', '.claude', 'memory', 'project_deals.md');

async function notionRequest(endpoint, method, body) {
  const res = await fetch(`https://api.notion.com/v1${endpoint}`, {
    method,
    headers: {
      'Authorization': `Bearer ${NOTION_API_KEY}`,
      'Notion-Version': '2022-06-28',
      'Content-Type': 'application/json',
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  return res.json();
}

function parseDealsFromMarkdown(markdown) {
  const deals = [];
  const lines = markdown.split('\n');
  let inTable = false;

  for (const line of lines) {
    if (line.includes('| Bien |')) { inTable = true; continue; }
    if (line.startsWith('|---')) continue;
    if (inTable && line.startsWith('|') && line.includes('€')) {
      const cols = line.split('|').map(c => c.trim()).filter(Boolean);
      if (cols.length >= 5) {
        deals.push({
          bien: cols[0],
          localisation: cols[1],
          prix: cols[2],
          statut: cols[3].replace(/[🔴🟡🟢✅]/u, '').trim(),
          notes: cols[5] || '',
        });
      }
    }
    if (inTable && !line.startsWith('|')) inTable = false;
  }
  return deals;
}

async function syncDealToNotion(deal) {
  if (!NOTION_API_KEY) {
    console.log(`[MOCK] Sync deal: ${deal.bien} — ${deal.localisation} (${deal.statut})`);
    return;
  }

  const payload = {
    parent: { database_id: NOTION_DATABASE_ID },
    properties: {
      Bien: { title: [{ text: { content: deal.bien } }] },
      Localisation: { rich_text: [{ text: { content: deal.localisation } }] },
      Prix: { rich_text: [{ text: { content: deal.prix } }] },
      Statut: { select: { name: deal.statut } },
      Notes: { rich_text: [{ text: { content: deal.notes } }] },
    }
  };

  const result = await notionRequest('/pages', 'POST', payload);
  console.log(`Sync OK: ${deal.bien} → Notion ID ${result.id}`);
}

async function run() {
  const markdown = fs.readFileSync(MEMORY_PATH, 'utf-8');
  const deals = parseDealsFromMarkdown(markdown);
  console.log(`${deals.length} deal(s) trouvé(s) dans project_deals.md`);

  for (const deal of deals) {
    await syncDealToNotion(deal);
  }

  console.log('Synchronisation terminée.');
}

run().catch(console.error);
