# Modèle vidéo « Chalet Reel » (OpenMontage / Remotion)

Montage de présentation d'un bien : visuels avec mouvement de caméra lent,
fondus enchaînés, carton final Douglas Elliman avec coordonnées et mention
« Visuels non contractuels ». Deux formats : 16:9 (1920×1080) et 9:16 (1080×1920).

Vidéos produites : `videos/chalet-megeve/`.

## Contenu

- `ChaletReel.tsx` : la composition (plans, durées, carton final, coordonnées).
- `Root.tsx.patch` : enregistre les compositions `ChaletMegeve` et `ChaletMegeveVertical`.
- `images/` : visuels utilisés (mentions d'origine retirées, page Megève sans « Lyell Lodge » ni « LVB »).

## Refaire le rendu

Dans une session où OpenMontage est installé (`/home/user/OpenMontage`) :

```bash
cd /home/user/OpenMontage/remotion-composer
cp /home/user/Douglas-Elliman-/video-templates/chalet-reel/ChaletReel.tsx src/
git apply /home/user/Douglas-Elliman-/video-templates/chalet-reel/Root.tsx.patch
mkdir -p public/chalet-megeve
cp /home/user/Douglas-Elliman-/video-templates/chalet-reel/images/* public/chalet-megeve/
npx remotion render src/index.tsx ChaletMegeve out-16x9.mp4 --codec h264 --crf 18
npx remotion render src/index.tsx ChaletMegeveVertical out-9x16.mp4 --codec h264 --crf 18
```

## Réutiliser pour un autre bien

Dans `ChaletReel.tsx` : remplacer les images dans `SHOTS` (chemin, durée,
zoom), et le texte du carton final (`EndCard`) ; coordonnées dans
`NAME`, `PHONE`, `CONTACT`.
