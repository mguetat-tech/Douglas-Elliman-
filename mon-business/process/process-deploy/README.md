# SOP — Déploiement site Netlify

## Quand utiliser ce process
À chaque mise à jour du site Douglas Elliman (nouvelles annonces, modification des pages).

## Étapes

### 1. Vérification locale
```bash
git status
git diff
```

### 2. Commit et push
```bash
git add -p
git commit -m "feat: description courte"
git push -u origin <branche>
```

### 3. Déploiement Netlify
- Netlify se déclenche automatiquement sur push vers `main`
- Vérifier le build sur : https://app.netlify.com
- Délai moyen : 1–2 minutes

### 4. Validation post-déploiement
- [ ] Tester sur mobile Safari (iPhone)
- [ ] Vérifier le formulaire de contact
- [ ] Vérifier que l'assistant IA répond correctement
- [ ] Tester les pages : index, estimation, assistant

### 5. En cas d'erreur de build
```bash
git revert HEAD
git push
```

## Variables d'environnement Netlify requises
- `ANTHROPIC_API_KEY` → clé API Claude (ne jamais committer)
