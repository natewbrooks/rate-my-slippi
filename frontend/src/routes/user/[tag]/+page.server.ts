import { error, type PageServerLoad } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params, fetch, setHeaders }) => {
  const res = await fetch(`/api/user/${params.tag}`, { headers: { accept: 'application/json' } });
  if (res.status === 304) {
    // Seldom hit in SvelteKit SSR, but safe guard
    return {};
  }
  if (!res.ok) throw error(res.status, 'User not found');

  // propagate caching hints to the client HTML
  setHeaders({
    'cache-control': 'public, max-age=60, stale-while-revalidate=120'
  });

  const { user, rank, char } = await res.json();
  return { user, rank, char };
};

// prevent client-side re-fetch on hydration/navigation if desired
export const csr = true;   // keep CSR, but data comes embedded from SSR
export const prerender = false;
