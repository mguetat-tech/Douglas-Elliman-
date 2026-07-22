import React, { useMemo } from "react";
import { interpolate, useCurrentFrame, useVideoConfig, random } from "remotion";
import { brand } from "./brand";

// Décor alpin abstrait (dégradé + crêtes + neige) avec effet Ken Burns lent.
// Aucune photo de bien n'étant disponible dans le repo, ce fond sert de
// toile de marque réutilisable en attendant de brancher de vrais visuels
// (voir <Img src={staticFile(...)} /> pour les remplacer plus tard).
export const AlpineBackground: React.FC<{ tint?: "royal" | "navy" | "teal" }> = ({
  tint = "navy",
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const zoom = interpolate(frame, [0, durationInFrames], [1, 1.12], {
    extrapolateRight: "clamp",
  });
  const drift = interpolate(frame, [0, durationInFrames], [0, -40]);

  const gradientFrom =
    tint === "teal" ? brand.teal : tint === "royal" ? brand.royal : brand.navy;

  const snow = useMemo(
    () =>
      new Array(70).fill(0).map((_, i) => ({
        x: random(`x-${i}`) * 100,
        y: random(`y-${i}`) * 100,
        r: 1 + random(`r-${i}`) * 2,
        seed: i,
      })),
    [],
  );

  return (
    <div
      style={{
        position: "absolute",
        inset: 0,
        overflow: "hidden",
        background: `linear-gradient(160deg, ${gradientFrom} 0%, ${brand.navy} 62%, #05060d 100%)`,
      }}
    >
      <div
        style={{
          position: "absolute",
          inset: -80,
          transform: `scale(${zoom}) translateX(${drift}px)`,
        }}
      >
        {/* Halo teal, signature de marque */}
        <div
          style={{
            position: "absolute",
            top: "-10%",
            right: "-15%",
            width: 900,
            height: 900,
            borderRadius: "50%",
            background: `radial-gradient(circle, ${brand.teal}55 0%, transparent 70%)`,
            filter: "blur(10px)",
          }}
        />

        {/* Crêtes alpines superposées */}
        <svg
          viewBox="0 0 1080 1920"
          width="1080"
          height="1920"
          style={{ position: "absolute", bottom: 0, left: -80 }}
          preserveAspectRatio="none"
        >
          <polygon
            points="0,1500 220,1250 420,1420 620,1180 860,1360 1080,1200 1240,1500 1240,1920 0,1920"
            fill="rgba(255,255,255,0.05)"
          />
          <polygon
            points="-100,1620 180,1400 380,1560 640,1320 900,1520 1240,1380 1240,1920 -100,1920"
            fill="rgba(255,255,255,0.09)"
          />
          <polygon
            points="-100,1750 260,1560 520,1700 780,1500 1080,1680 1240,1600 1240,1920 -100,1920"
            fill="rgba(255,255,255,0.14)"
          />
        </svg>

        {/* Neige / grain */}
        {snow.map((s) => {
          const flicker =
            0.25 + 0.5 * Math.abs(Math.sin((frame + s.seed * 13) / 40));
          return (
            <div
              key={s.seed}
              style={{
                position: "absolute",
                left: `${s.x}%`,
                top: `${s.y}%`,
                width: s.r,
                height: s.r,
                borderRadius: "50%",
                background: "#fff",
                opacity: flicker * 0.6,
              }}
            />
          );
        })}
      </div>

      {/* Vignette */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "radial-gradient(ellipse at center, transparent 45%, rgba(0,0,0,0.45) 100%)",
        }}
      />
    </div>
  );
};
