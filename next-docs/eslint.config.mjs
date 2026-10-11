import nextVitals from 'eslint-config-next/core-web-vitals'
import nextTs from 'eslint-config-next/typescript'

/** @type {import('eslint').Linter.Config[]} */
const eslintConfig = [
  ...nextVitals,
  ...nextTs,
  {
    rules: {
      // Keep prior baseline: `any` is used intentionally in several adapters.
      '@typescript-eslint/no-explicit-any': 'warn',
    },
  },
  {
    // Node CommonJS helper/test scripts use require().
    files: ['**/*.js', '**/*.cjs'],
    rules: {
      '@typescript-eslint/no-require-imports': 'off',
    },
  },
  {
    ignores: ['.next/**', 'out/**', 'build/**', 'next-env.d.ts', '**/*.mdx'],
  },
]

export default eslintConfig
