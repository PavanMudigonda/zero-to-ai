import type { ReactNode } from 'react';

type HubAction = {
  label: string;
  href: string;
  variant?: 'primary' | 'secondary' | 'ghost';
};

type HubStat = {
  label: string;
  value: string;
  description: string;
};

type HubFeature = {
  eyebrow: string;
  title: string;
  description: string;
  href: string;
  cta: string;
  accent: string;
};

type HubHeroProps = {
  badges: string[];
  badgeToneClass: string;
  eyebrow: string;
  eyebrowClass: string;
  title: string;
  description: string;
  actions: HubAction[];
  stats: HubStat[];
  backgroundClass: string;
  shadowClass: string;
  statLabelClass: string;
  statDescriptionClass: string;
};

type HubSectionIntroProps = {
  eyebrow: string;
  title: string;
  href: string;
  hrefLabel: string;
  accentClass: string;
};

function actionClass(variant: HubAction['variant'] = 'secondary'): string {
  if (variant === 'primary') {
    return 'inline-flex items-center justify-center rounded-xl bg-sky-400 px-6 py-3 text-base font-semibold text-slate-950 transition hover:bg-sky-300';
  }

  if (variant === 'ghost') {
    return 'inline-flex items-center justify-center rounded-xl border border-white/15 bg-transparent px-6 py-3 text-base font-semibold text-slate-200 transition hover:bg-white/8';
  }

  return 'inline-flex items-center justify-center rounded-xl border border-white/15 bg-white/8 px-6 py-3 text-base font-semibold text-white transition hover:bg-white/14';
}

export function HubPageShell({ children }: { children: ReactNode }) {
  return <div className="mx-auto max-w-6xl px-4 py-8 sm:px-6 lg:px-8">{children}</div>;
}

export function HubHero({
  badges,
  badgeToneClass,
  eyebrow,
  eyebrowClass,
  title,
  description,
  actions,
  stats,
  backgroundClass,
  shadowClass,
  statLabelClass,
  statDescriptionClass,
}: HubHeroProps) {
  return (
    <section className={`overflow-hidden rounded-[2rem] border border-slate-200 px-6 py-10 text-white sm:px-10 sm:py-14 ${backgroundClass} ${shadowClass}`}>
      <div className={`flex flex-wrap gap-3 text-sm font-medium ${badgeToneClass}`}>
        {badges.map((badge) => (
          <span key={badge} className="rounded-full border border-white/15 bg-white/8 px-3 py-1">
            {badge}
          </span>
        ))}
      </div>

      <div className="mt-8 grid gap-10 lg:grid-cols-[minmax(0,1.4fr)_minmax(280px,0.9fr)] lg:items-end">
        <div>
          <p className={`text-sm font-semibold uppercase tracking-[0.22em] ${eyebrowClass}`}>{eyebrow}</p>
          <h1 className="mt-4 max-w-3xl text-4xl font-black tracking-tight text-white sm:text-6xl">{title}</h1>
          <p className="mt-5 max-w-2xl text-lg leading-8 text-slate-200/90 sm:text-xl">{description}</p>

          <div className="mt-8 flex flex-wrap gap-4">
            {actions.map((action) => (
              <a key={action.href} href={action.href} className={actionClass(action.variant)}>
                {action.label}
              </a>
            ))}
          </div>
        </div>

        <div className="grid gap-4 rounded-3xl border border-white/10 bg-white/8 p-5 backdrop-blur-sm sm:grid-cols-3 lg:grid-cols-1">
          {stats.map((stat) => (
            <div key={stat.label}>
              <p className={`text-xs font-semibold uppercase tracking-[0.2em] ${statLabelClass}`}>{stat.label}</p>
              <p className="mt-2 text-2xl font-bold">{stat.value}</p>
              <p className={`mt-1 text-sm ${statDescriptionClass}`}>{stat.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export function HubFeatureCard({ feature }: { feature: HubFeature }) {
  return (
    <a
      href={feature.href}
      className="group rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-xl dark:border-slate-800 dark:bg-slate-900/60"
    >
      <p className={`text-sm font-semibold uppercase tracking-[0.18em] ${feature.accent}`}>{feature.eyebrow}</p>
      <h2 className="mt-3 text-2xl font-bold text-slate-900 dark:text-white">{feature.title}</h2>
      <p className="mt-3 text-sm leading-7 text-slate-600 dark:text-slate-300">{feature.description}</p>
      <span className="mt-5 inline-flex text-sm font-semibold text-slate-900 dark:text-slate-100">{feature.cta} →</span>
    </a>
  );
}

export function HubSectionIntro({ eyebrow, title, href, hrefLabel, accentClass }: HubSectionIntroProps) {
  return (
    <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
      <div>
        <p className={`text-sm font-semibold uppercase tracking-[0.18em] ${accentClass}`}>{eyebrow}</p>
        <h2 className="mt-2 text-3xl font-bold tracking-tight text-slate-900 dark:text-white">{title}</h2>
      </div>
      <a href={href} className="text-sm font-semibold text-slate-700 underline decoration-slate-300 underline-offset-4 hover:text-sky-700 dark:text-slate-200 dark:decoration-slate-700 dark:hover:text-sky-300">
        {hrefLabel}
      </a>
    </div>
  );
}