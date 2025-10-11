import type { PageLoad } from "./$types";

export const load: PageLoad = async ({ params, url, fetch, depends, data }) => {
  const view = url.searchParams.get("view") ?? "reviews";
  depends("user:view");

  let reviews: unknown = null;
  if (view === "reviews") {
    const res = await fetch(`/api/reviews/${encodeURIComponent(params.tag)}`);
    if (!res.ok) throw new Error(`Failed to load reviews for ${params.tag}`);
    reviews = await res.json();
  }

  // IMPORTANT: merge server data into the return
  return {
    ...data,              // <-- brings in { user, rank, char } from +page.server.ts
    tag: params.tag,
    view,
    reviews
  };
};
