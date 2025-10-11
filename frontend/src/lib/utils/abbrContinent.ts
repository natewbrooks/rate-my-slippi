export function abbreviateContinent(continent: string | null | undefined): string {
  if (!continent) return "UNK";

  const mapping: Record<string, string> = {
    NORTH_AMERICA: "NA",
    SOUTH_AMERICA: "SA",
    EUROPE: "EU",
    ASIA: "AS",
    AFRICA: "AF",
    OCEANIA: "OC",
    ANTARCTICA: "AN"
  };

  const key = continent.toUpperCase().replace(/\s+/g, "_");
  return mapping[key] ?? "UNK";
}
