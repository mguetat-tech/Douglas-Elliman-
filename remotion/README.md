# Remotion video

<p align="center">
  <a href="https://github.com/remotion-dev/logo">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github.com/remotion-dev/logo/raw/main/animated-logo-banner-dark.apng">
      <img alt="Animated Remotion Logo" src="https://github.com/remotion-dev/logo/raw/main/animated-logo-banner-light.gif">
    </picture>
  </a>
</p>

Welcome to your Remotion project!

## Reels Douglas Elliman Megève

Ce projet contient un composant réutilisable `PropertyReel` (voir
`src/PropertyReel.tsx`) qui génère un reel Instagram vertical (1080x1920) :
logo → accroche → slides de texte → CTA + coordonnées, sur un décor alpin
animé (`src/AlpineBackground.tsx`), avec les polices et couleurs de marque
(`src/brand.ts`, `src/fonts.ts`).

Trois reels sont déjà enregistrés dans `src/Composition.tsx`, à partir des
textes des posts 1, 4 et 9 de `index.html` :

- `ReelOuverture`
- `ReelMiroirIdentitaire`
- `ReelExpatrie`

Pour créer un nouveau reel : ajouter un objet dans `src/presets.ts` (kicker,
hook, slides, cta, ctaSub, hashtags), puis l'enregistrer avec une nouvelle
`<Composition>` dans `src/Composition.tsx`.

Rendu :

```console
npx remotion render src/index.ts ReelOuverture out/reel-ouverture.mp4
```

## Commands

**Install Dependencies**

```console
npm i
```

**Start Preview**

```console
npm run dev
```

**Render video**

```console
npx remotion render
```

**Upgrade Remotion**

```console
npx remotion upgrade
```

## Docs

Get started with Remotion by reading the [fundamentals page](https://www.remotion.dev/docs/the-fundamentals).

## Help

We provide help on our [Discord server](https://discord.gg/6VzzNDwUwV).

## Issues

Found an issue with Remotion? [File an issue here](https://github.com/remotion-dev/remotion/issues/new).

## License

Note that for some entities a company license is needed. [Read the terms here](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md).
