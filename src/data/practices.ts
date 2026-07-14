/**
 * Practice areas — shared by the Home grid and the Practice Areas page.
 * Editable. The firm is full-service with Personal Injury as the flagship.
 *
 * Fee messaging (Texas Disciplinary Rules Part VII, §5 of the README):
 *   - `contingency: true`         → the plain "no fee unless we obtain a
 *                                    recovery" block (injury matters only).
 *   - `contingencyOptional: true` → a *qualified* block: contingency is one of
 *                                    several possible fee arrangements, so the
 *                                    "no fee unless we win" promise is conditional.
 *   - neither flag                → flat/hourly note; must not imply "no fee
 *                                    unless we win."
 * Never use specialist / expert / certified language in any `detail`.
 */
export interface Practice {
  slug: string;
  title: string;
  icon: IconName;
  /** Short line for the Home grid card. */
  blurb: string;
  /** Fuller, non-promissory paragraph for the Practice Areas page. */
  detail: string;
  /** Bullet items shown on the Practice Areas page (optional). */
  points?: string[];
  /** Injury matters handled purely on contingency. */
  contingency?: boolean;
  /** Contingency is available but not the only fee model (e.g. insurance). */
  contingencyOptional?: boolean;
  flagship?: boolean;
}

export type IconName =
  | 'injury'
  | 'wrongful-death'
  | 'insurance'
  | 'business'
  | 'contract'
  | 'family'
  | 'consumer-debt'
  | 'estate'
  | 'probate'
  | 'litigation'
  | 'landlord';

export const PRACTICES: Practice[] = [
  {
    slug: 'personal-injury',
    title: 'Personal Injury',
    icon: 'injury',
    flagship: true,
    contingency: true,
    blurb:
      'Car & truck collisions, 18-wheeler crashes, premises liability, and product injuries.',
    detail:
      'The firm’s flagship practice. If you have been hurt because of someone else’s negligence, you deserve straightforward answers and a lawyer who handles your case directly. Having spent years defending corporations and insurers in serious injury cases, the firm now puts that same understanding to work for injured people — anticipating how the other side thinks while pursuing fair compensation for medical bills, lost income, and the disruption an injury causes.',
    points: [
      'Car and truck collisions',
      '18-wheeler and commercial fleet crashes',
      'Oilfield and industrial workplace accidents',
      'Premises liability (unsafe property conditions)',
      'Product-related injuries',
      'Catastrophic and Gulf Coast industrial accidents',
    ],
  },
  {
    slug: 'wrongful-death',
    title: 'Wrongful Death',
    icon: 'wrongful-death',
    contingency: true,
    blurb:
      'Compassionate representation for families after a preventable loss.',
    detail:
      'When a family loses someone because of another’s negligence, the practical and financial questions can feel overwhelming at the worst possible time. The firm handles wrongful death matters with care and discretion, helping surviving family members understand their options and pursue accountability for the loss.',
  },
  {
    slug: 'insurance-disputes',
    title: 'Insurance Disputes',
    icon: 'insurance',
    contingencyOptional: true,
    blurb:
      'Fighting denied, delayed, and underpaid claims — including bad-faith disputes.',
    detail:
      'Insurance companies do not always pay what they owe. The firm represents policyholders in first-party property claims and bad-faith disputes — the denied, delayed, and underpaid claims that leave families and businesses holding the bill. Depending on the matter, these cases are handled on a contingency-fee or hourly basis, and the firm will explain which arrangement applies before you commit.',
    points: [
      'Denied and underpaid first-party property claims',
      'Delayed claim handling',
      'Bad-faith and unfair claim-practice disputes',
    ],
  },
  {
    slug: 'business-commercial',
    title: 'Business & Commercial',
    icon: 'business',
    blurb:
      'Entity formation and commercial disputes for small businesses and their owners.',
    detail:
      'From forming a new entity to resolving a dispute that threatens the business you built, the firm advises small businesses and their owners on the practical decisions that keep a company on solid footing. Business and commercial matters are handled on a flat or hourly basis, with the scope and cost discussed up front.',
    points: [
      'Entity formation (LLCs, partnerships, corporations)',
      'Owner, partner, and vendor disputes',
      'Commercial and business litigation',
    ],
  },
  {
    slug: 'contract-drafting-review',
    title: 'Contract Drafting & Review',
    icon: 'contract',
    blurb:
      'Clear contracts drafted and reviewed before you sign — not after.',
    detail:
      'A contract is easiest to fix before it is signed. The firm drafts and reviews agreements for individuals and small businesses, translating dense terms into plain language and flagging the risks that matter to you. This work is handled on a flat or hourly basis, quoted before the work begins.',
  },
  {
    slug: 'family-law',
    title: 'Family Law',
    icon: 'family',
    blurb:
      'Divorce, custody, support, and modifications, handled with discretion.',
    detail:
      'Family matters are personal, and they deserve a lawyer who listens before advising. The firm handles divorce, child custody and support, and post-judgment modifications with candor and discretion, helping you understand the realistic path ahead. Family law matters are handled on a flat or hourly basis depending on the situation.',
    points: [
      'Divorce',
      'Child custody and possession',
      'Child and spousal support',
      'Modifications and enforcement',
    ],
  },
  {
    slug: 'consumer-debt-defense',
    title: 'Consumer & Debt Defense',
    icon: 'consumer-debt',
    blurb:
      'Defense against debt-collection suits and consumer-protection matters.',
    detail:
      'Being sued by a debt collector is stressful, but you have rights — and you do not have to face it alone. The firm defends individuals against debt-collection lawsuits and handles consumer-protection matters, working toward a resolution that fits your circumstances. These matters are handled on a flat or hourly basis.',
  },
  {
    slug: 'estate-planning',
    title: 'Estate Planning & Wills',
    icon: 'estate',
    blurb: 'Wills and foundational planning to protect your family’s future.',
    detail:
      'Thoughtful planning gives your family clarity and reduces stress later. The firm helps individuals and families put practical documents in place — wills and related foundational planning — tailored to your situation. Consultations are available; fees are typically flat or hourly depending on the work.',
  },
  {
    slug: 'probate-guardianship',
    title: 'Probate & Guardianship',
    icon: 'probate',
    blurb:
      'Guiding families through probate, estate administration, and guardianships.',
    detail:
      'After a loss, or when a loved one can no longer manage their own affairs, the legal steps can feel daunting. The firm guides families through probate, estate administration, and guardianship proceedings, keeping the process as clear and orderly as possible. This work is handled on a flat or hourly basis.',
  },
  {
    slug: 'civil-litigation',
    title: 'Civil Litigation',
    icon: 'litigation',
    blurb: 'Practical representation in disputes and civil court matters.',
    detail:
      'Disputes happen. When they do, you want a lawyer who will give you a candid assessment and represent your interests efficiently. The firm handles a range of civil litigation matters and will discuss the likely path and costs up front. Fees are typically flat or hourly depending on the matter.',
  },
  {
    slug: 'landlord-tenant',
    title: 'Landlord–Tenant / Real Estate',
    icon: 'landlord',
    blurb: 'Guidance for landlords, tenants, and real-property disputes.',
    detail:
      'Whether you are a property owner or a tenant, real-property issues are easier to resolve with clear guidance. The firm advises on landlord–tenant matters and related real estate questions, with fees typically flat or hourly depending on the work involved.',
  },
];
