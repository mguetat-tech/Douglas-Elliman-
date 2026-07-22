import React from "react";

// Monogramme "DE" recréé en SVG (cf. header .header-logo dans index.html),
// pour pouvoir le recolorer (currentColor) sur fond navy/royal.
export const DELogo: React.FC<{ size?: number; color?: string }> = ({
  size = 100,
  color = "#fff",
}) => {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 100 100"
      style={{ color, display: "block" }}
    >
      <circle
        cx={50}
        cy={50}
        r={46}
        fill="none"
        stroke="currentColor"
        strokeWidth={3}
      />
      <line
        x1={50}
        y1={16}
        x2={50}
        y2={84}
        stroke="currentColor"
        strokeWidth={3.5}
      />
      <path
        d="M50,18 A32,32 0 0,0 50,82"
        fill="none"
        stroke="currentColor"
        strokeWidth={3.5}
      />
      <line
        x1={50}
        y1={18}
        x2={78}
        y2={18}
        stroke="currentColor"
        strokeWidth={3.5}
      />
      <line
        x1={50}
        y1={50}
        x2={73}
        y2={50}
        stroke="currentColor"
        strokeWidth={3.5}
      />
      <line
        x1={50}
        y1={82}
        x2={78}
        y2={82}
        stroke="currentColor"
        strokeWidth={3.5}
      />
    </svg>
  );
};
