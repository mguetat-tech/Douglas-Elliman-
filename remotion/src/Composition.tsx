import { CalculateMetadataFunction, Composition } from "remotion";
import { PropertyReel, PropertyReelProps, getPropertyReelDuration, FPS } from "./PropertyReel";
import { reelOuverture, reelMiroirIdentitaire, reelExpatrie } from "./presets";

const calculateMetadata: CalculateMetadataFunction<PropertyReelProps> = ({
  props,
}) => {
  return { durationInFrames: getPropertyReelDuration(props) };
};

// Trois reels Instagram (format 9:16) prêts à rendre, à partir des textes
// déjà rédigés dans index.html (posts 1, 4 et 9). Pour un nouveau bien,
// dupliquer un preset dans presets.ts avec un nouveau texte.
export const PropertyReels = () => (
  <>
    <Composition
      id="ReelOuverture"
      component={PropertyReel}
      fps={FPS}
      width={1080}
      height={1920}
      durationInFrames={getPropertyReelDuration(reelOuverture)}
      defaultProps={reelOuverture}
      calculateMetadata={calculateMetadata}
    />
    <Composition
      id="ReelMiroirIdentitaire"
      component={PropertyReel}
      fps={FPS}
      width={1080}
      height={1920}
      durationInFrames={getPropertyReelDuration(reelMiroirIdentitaire)}
      defaultProps={reelMiroirIdentitaire}
      calculateMetadata={calculateMetadata}
    />
    <Composition
      id="ReelExpatrie"
      component={PropertyReel}
      fps={FPS}
      width={1080}
      height={1920}
      durationInFrames={getPropertyReelDuration(reelExpatrie)}
      defaultProps={reelExpatrie}
      calculateMetadata={calculateMetadata}
    />
  </>
);
