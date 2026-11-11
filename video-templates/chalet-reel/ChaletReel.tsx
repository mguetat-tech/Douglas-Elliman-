import React from "react";
import {
  AbsoluteFill,
  Easing,
  Img,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadPlayfair, loadSpaceGrotesk } from "./lib/localFonts";

const { fontFamily: serif } = loadPlayfair("normal", ["400"]);
const { fontFamily: sans } = loadSpaceGrotesk(["400"]);
export const CONTACT = "mathias.guetat@elliman.fr";
const NAME = "Mathias Guetat";
const PHONE = "06 74 67 10 44";
const BAND = 0; // px: black strip under the photos (landscape) for the legal mention

type Layout = "landscape" | "vertical";

export type ChaletReelProps = {
  layout: Layout;
};

const FADE = 0.6; // seconds of cross-dissolve between shots
const ease = Easing.bezier(0.33, 0, 0.2, 1);

// One still with a slow camera move. `overlay` fades in on top mid-shot.
const Still: React.FC<{
  src: string;
  overlay?: { src: string; at: number };
  from: number;
  to: number;
  layout: Layout;
  fadeIn: number;
  dur: number;
  page?: boolean; // brochure page: show whole, never cropped
  contact?: boolean; // last photo: full contact block
}> = ({ src, overlay, from, to, layout, fadeIn, dur, page, contact }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = interpolate(frame, [0, dur * fps], [0, 1], { extrapolateRight: "clamp" });
  const scale = interpolate(t, [0, 1], [from, to], { easing: ease });
  const opacity = interpolate(frame, [0, fadeIn * fps], [0, 1], {
    extrapolateRight: "clamp",
  });
  const overlayOpacity = overlay
    ? interpolate(frame, [overlay.at * fps, (overlay.at + 1.2) * fps], [0, 1], {
        extrapolateLeft: "clamp",
        extrapolateRight: "clamp",
        easing: ease,
      })
    : 0;

  // Landscape: full width, anchored to the bottom so the baked-in captions
  // (lower third) are never cropped; any crop comes off the sky/ceiling.
  // Vertical: image contained in the middle over a blurred, darkened copy.
  const fg: React.CSSProperties = page
    ? layout === "landscape"
      ? { position: "absolute", top: 0, height: "100%", left: "50%", aspectRatio: "1160 / 831", translate: "-50% 0", transformOrigin: "50% 50%" }
      : { position: "absolute", left: 0, top: "50%", width: "100%", translate: "0 -50%", transformOrigin: "50% 50%" }
    : layout === "landscape"
      ? { position: "absolute", left: 0, bottom: BAND, width: "100%", transformOrigin: "50% 100%" }
      : { position: "absolute", left: "-10%", top: "50%", width: "120%", translate: "0 -50%", transformOrigin: "50% 50%" };

  return (
    <AbsoluteFill style={{ opacity, backgroundColor: page && layout === "landscape" ? "#ffffff" : "#0b0a09", overflow: "hidden" }}>
      {layout === "vertical" && (
        <Img
          src={staticFile(src)}
          style={{
            position: "absolute",
            inset: -80,
            width: "calc(100% + 160px)",
            height: "calc(100% + 160px)",
            objectFit: "cover",
            filter: `blur(40px) brightness(${page ? 0.18 : 0.45})`,
            transform: `scale(${1.1 + (scale - 1)})`,
          }}
        />
      )}
      <div style={{ ...fg, transform: `scale(${scale})` }}>
        <Img src={staticFile(src)} style={{ width: "100%", height: page && layout === "landscape" ? "100%" : undefined, display: "block" }} />
        {overlay && (
          <Img
            src={staticFile(overlay.src)}
            style={{ position: "absolute", inset: 0, width: "100%", opacity: overlayOpacity }}
          />
        )}
      </div>
    </AbsoluteFill>
  );
};

const EndCard: React.FC<{ layout: Layout }> = ({ layout }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const v = layout === "vertical";
  const appear = (delay: number) => ({
    opacity: interpolate(frame, [delay * fps, (delay + 1) * fps], [0, 1], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }),
    transform: `translateY(${interpolate(frame, [delay * fps, (delay + 1) * fps], [12, 0], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
      easing: ease,
    })}px)`,
  });
  const caps: React.CSSProperties = {
    fontFamily: serif,
    color: "#e9e3d8",
    textTransform: "uppercase",
    textAlign: "center",
  };
  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#0b0a09",
        justifyContent: "center",
        alignItems: "center",
        opacity: interpolate(frame, [0, FADE * fps], [0, 1], { extrapolateRight: "clamp" }),
      }}
    >
      <div style={{ ...caps, ...appear(0.3), fontSize: v ? 64 : 76, letterSpacing: v ? 14 : 22 }}>
        Douglas Elliman
      </div>
      <div style={{ ...appear(0.8), width: 90, height: 1, background: "#b9a788", margin: v ? "44px 0" : "40px 0" }} />
      <div style={{ ...caps, ...appear(1.1), fontSize: v ? 30 : 30, letterSpacing: v ? 9 : 12, color: "#b9a788" }}>
        Megève · Off-market
      </div>
      <div
        style={{
          ...appear(1.8),
          marginTop: v ? 96 : 60,
          fontFamily: sans,
          color: "#e9e3d8",
          textAlign: "center",
          fontSize: v ? 30 : 26,
          letterSpacing: 1,
          lineHeight: 1.6,
        }}
      >
        <div style={{ fontFamily: serif, fontSize: v ? 42 : 36, letterSpacing: 3, marginBottom: 8 }}>{NAME}</div>
        <div style={{ fontSize: v ? 34 : 28 }}>{PHONE}</div>
        <div>{CONTACT}</div>
      </div>
      <div
        style={{
          ...appear(1.8),
          position: "absolute",
          right: v ? 28 : 24,
          bottom: v ? 24 : 14,
          fontFamily: sans,
          fontSize: v ? 16 : 13,
          letterSpacing: 0.4,
          color: "rgba(255,255,255,0.55)",
        }}
      >
        Visuels non contractuels
      </div>
    </AbsoluteFill>
  );
};

// Timeline in seconds: [start, duration]
const SHOTS = [
  { start: 0, dur: 6.5, src: "chalet-megeve/1-exterieur-clean.jpg", from: 1.08, to: 1.0, fadeIn: 1.0 },
  { start: 5.9, dur: 5.6, src: "chalet-megeve/2-salon-clean.jpg", from: 1.0, to: 1.06, fadeIn: FADE },
  { start: 10.9, dur: 6.1, src: "chalet-megeve/3a-situation.jpg", from: 0.96, to: 1.0, fadeIn: FADE, page: true },
  { start: 16.4, dur: 5.6, src: "chalet-megeve/3b-suites-clean.jpg", from: 1.06, to: 1.0, fadeIn: FADE },
  { start: 21.4, dur: 6.6, src: "chalet-megeve/4-piscine-clean.jpg", from: 1.06, to: 1.0, fadeIn: FADE, contact: true },
];
export const CHALET_REEL_SECONDS = 34;

export const ChaletReel: React.FC<ChaletReelProps> = ({ layout }) => {
  const { fps, durationInFrames } = useVideoConfig();
  const frame = useCurrentFrame();
  const fadeOut = interpolate(frame, [durationInFrames - fps, durationInFrames], [1, 0], {
    extrapolateLeft: "clamp",
  });
  return (
    <AbsoluteFill style={{ backgroundColor: "#0b0a09", opacity: fadeOut }}>
      {SHOTS.map((s) => (
        <Sequence key={s.src} from={Math.round(s.start * fps)} durationInFrames={Math.round(s.dur * fps)}>
          <Still {...s} layout={layout} />
        </Sequence>
      ))}
      <Sequence from={Math.round(27.4 * fps)}>
        <EndCard layout={layout} />
      </Sequence>
    </AbsoluteFill>
  );
};
