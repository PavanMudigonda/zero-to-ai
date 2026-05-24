This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

This app includes a progress sync widget backed by Supabase Auth and a `learning_progress` table. The `Sync with Google` button in the UI calls Supabase OAuth and then returns to `/auth/callback` in this app.

### Supabase and Google OAuth setup

1. Create a Supabase project.
2. In Supabase, copy the project URL and anon key from `Settings -> API`.
3. In `next-docs`, create `.env.local` from `.env.local.example` and fill in:

```bash
NEXT_PUBLIC_SUPABASE_URL=https://YOUR_PROJECT_REF.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY
```

4. In Supabase, open `Authentication -> URL Configuration` and set:

```text
Site URL: http://localhost:3000
Additional Redirect URLs:
http://localhost:3000/auth/callback
https://your-production-domain/auth/callback
```

5. In Google Cloud Console:
	- Create or select a project.
	- Open `APIs & Services -> OAuth consent screen` and configure the app.
	- Open `APIs & Services -> Credentials` and create an `OAuth client ID` with application type `Web application`.
	- Add authorized JavaScript origins:

```text
http://localhost:3000
https://your-production-domain
```

	- Add the Google redirect URI that points back to Supabase, not to this Next.js app:

```text
https://YOUR_PROJECT_REF.supabase.co/auth/v1/callback
```

6. In Supabase, open `Authentication -> Providers -> Google`, enable Google, and paste the Google client ID and client secret.
7. Create the progress table and RLS policies by running [scripts/supabase-learning-progress.sql](./scripts/supabase-learning-progress.sql) in the Supabase SQL editor.
8. Start the app with `npm run dev` and test `Sync with Google` on `http://localhost:3000`.

### Common failure points

- If the button shows `Supabase URL and Anon Key are missing in .env.local`, the local env file is missing or incomplete.
- If Google says `redirect_uri_mismatch`, the Google OAuth client is missing `https://YOUR_PROJECT_REF.supabase.co/auth/v1/callback`.
- If Supabase login succeeds but sync fails, the `learning_progress` table or its RLS policies are missing.
- If production login returns to the wrong host, add the production `/auth/callback` URL in Supabase `Additional Redirect URLs`.

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
