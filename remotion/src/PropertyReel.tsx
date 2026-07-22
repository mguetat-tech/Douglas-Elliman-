import React from "react";
import {
  AbsoluteFill,
  Sequence,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { brand } from "./brand";
import { AlpineBackground } from "./AlpineBackground";
import { DELogo } from "./DELogo";
import { serifFont, sansFont } from "./fonts";

export const FPS = 30;
export const INTRO_FRAMES = 45;
export const HOOK_FRAMES = 120;
export const SLIDE_FRAMES = 90;
export const CTA_FRAMES = 150;

export type PropertyReelProps = {
  kicker: string;
  hook: string;
  slides: string[];
  cta: string;
  ctaSub: string;
  hashtags: string[];
};

export const getPropertyReelDuration = (props: PropertyReelProps) =>
  INTRO_FRAMES + HOOK_FRAMES + props.slides.length * SLIDE_FRAMES + CTA_FRAMES;

const Eyebrow: React.FC<{ children: React.ReactNode; style?: React.CSSProperties }> = ({
  children,
  style,
}) => (
  <div
    style={{
      fontFamily: sansFont,
      fontSize: 22,
      fontWeight: 500,
      letterSpacing: 8,
      textTransform: "uppercase",
      color: "rgba(255,255,255,0.85)",
      ...style,
    }}
  >
    {children}
  </div>
);

const fadeSpring = (frame: number, fps: number, delay = 0) =>
  spring({ frame: frame - delay, fps, config: { damping: 200 } });

const Intro: React.FC<{ kicker: string }> = ({ kicker }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const logoIn = spring({ frame, fps, config: { damping: 12, mass: 0.6 } });
  const textOpacity = interpolate(frame, [15, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "center" }}>
      <div style={{ transform: `scale(${logoIn})`, marginBottom: 36 }}>
        <DELogo size={140} color="#fff" />
      </div>
      <div style={{ opacity: textOpacity }}>
        <Eyebrow>{kicker}</Eyebrow>
      </div>
    </AbsoluteFill>
  );
};

const Hook: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const scale = fadeSpring(frame, fps);
  const opacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const exitOpacity = interpolate(
    frame,
    [durationInFrames - 18, durationInFrames],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  return (
    <AbsoluteFill
      style={{
        alignItems: "center",
        justifyContent: "center",
        padding: "0 90px",
      }}
    >
      <div
        style={{
          opacity: opacity * exitOpacity,
          transform: `scale(${0.9 + scale * 0.1})`,
          fontFamily: serifFont,
          fontWeight: 400,
          fontSize: 74,
          lineHeight: 1.22,
          color: "#fff",
          textAlign: "center",
          whiteSpace: "pre-line",
        }}
      >
        {text}
      </div>
    </AbsoluteFill>
  );
};

const Slide: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const opacity = interpolate(frame, [0, 18], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const exitOpacity = interpolate(
    frame,
    [durationInFrames - 15, durationInFrames],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );
  const translateY = interpolate(frame, [0, 18], [24, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        alignItems: "center",
        justifyContent: "center",
        padding: "0 100px",
      }}
    >
      <div
        style={{
          opacity: opacity * exitOpacity,
          transform: `translateY(${translateY}px)`,
          fontFamily: serifFont,
          fontWeight: 300,
          fontSize: 52,
          lineHeight: 1.4,
          color: "#fff",
          textAlign: "center",
          whiteSpace: "pre-line",
        }}
      >
        {text}
      </div>
    </AbsoluteFill>
  );
};

const Outro: React.FC<{ cta: string; ctaSub: string; hashtags: string[] }> = ({
  cta,
  ctaSub,
  hashtags,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const ctaOpacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const logoScale = spring({ frame: frame - 45, fps, config: { damping: 14 } });
  const barWidth = interpolate(frame, [55, 80], [0, 220], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const tagsOpacity = interpolate(frame, [70, 95], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        alignItems: "center",
        justifyContent: "center",
        padding: "0 90px",
        textAlign: "center",
      }}
    >
      <div
        style={{
          opacity: ctaOpacity,
          fontFamily: serifFont,
          fontWeight: 400,
          fontStyle: "italic",
          fontSize: 58,
          lineHeight: 1.3,
          color: "#fff",
          marginBottom: 28,
          whiteSpace: "pre-line",
        }}
      >
        {cta}
      </div>
      <div
        style={{
          opacity: ctaOpacity,
          fontFamily: sansFont,
          fontSize: 24,
          letterSpacing: 1,
          color: brand.teal,
          marginBottom: 56,
        }}
      >
        {ctaSub}
      </div>

      <div style={{ transform: `scale(${logoScale})`, marginBottom: 20 }}>
        <DELogo size={100} color="#fff" />
      </div>
      <div
        style={{
          width: barWidth,
          height: 1,
          background: "rgba(255,255,255,0.4)",
          marginBottom: 20,
        }}
      />
      <div
        style={{
          fontFamily: serifFont,
          fontWeight: 300,
          fontSize: 34,
          letterSpacing: 5,
          textTransform: "uppercase",
          color: "#fff",
          marginBottom: 6,
        }}
      >
        {brand.wordmark}
      </div>
      <div
        style={{
          fontFamily: sansFont,
          fontSize: 16,
          letterSpacing: 4,
          textTransform: "uppercase",
          color: "rgba(255,255,255,0.75)",
          marginBottom: 44,
        }}
      >
        {brand.wordmarkSub}
      </div>

      <div
        style={{
          opacity: tagsOpacity,
          fontFamily: sansFont,
          fontSize: 15,
          letterSpacing: 0.5,
          color: "rgba(255,255,255,0.55)",
          maxWidth: 780,
        }}
      >
        {hashtags.join("  ")}
      </div>
    </AbsoluteFill>
  );
};

export const PropertyReel: React.FC<PropertyReelProps> = ({
  kicker,
  hook,
  slides,
  cta,
  ctaSub,
  hashtags,
}) => {
  let cursor = 0;
  const introAt = cursor;
  cursor += INTRO_FRAMES;
  const hookAt = cursor;
  cursor += HOOK_FRAMES;
  const slideStarts = slides.map(() => {
    const at = cursor;
    cursor += SLIDE_FRAMES;
    return at;
  });
  const outroAt = cursor;

  return (
    <AbsoluteFill style={{ backgroundColor: brand.navy }}>
      <AlpineBackground tint="navy" />

      <Sequence from={introAt} durationInFrames={INTRO_FRAMES}>
        <Intro kicker={kicker} />
      </Sequence>

      <Sequence from={hookAt} durationInFrames={HOOK_FRAMES}>
        <Hook text={hook} />
      </Sequence>

      {slides.map((text, i) => (
        <Sequence key={i} from={slideStarts[i]} durationInFrames={SLIDE_FRAMES}>
          <Slide text={text} />
        </Sequence>
      ))}

      <Sequence from={outroAt} durationInFrames={CTA_FRAMES}>
        <Outro cta={cta} ctaSub={ctaSub} hashtags={hashtags} />
      </Sequence>

      {/* Bandeau de marque permanent, discret, comme sur les visuels du site */}
      <AbsoluteFill
        style={{
          alignItems: "center",
          justifyContent: "flex-start",
          paddingTop: 64,
          pointerEvents: "none",
        }}
      >
        <div
          style={{
            fontFamily: sansFont,
            fontSize: 15,
            letterSpacing: 5,
            textTransform: "uppercase",
            color: "rgba(255,255,255,0.55)",
          }}
        >
          {brand.handle}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
