/**
 * Practice areas — shared by the Home grid and the Practice Areas page.
 * Editable. Personal Injury is the flagship; only injury areas carry
 * contingency messaging (`contingency: true`).
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
  contingency?: boolean;
  flagship?: boolean;
}

export type IconName =
  | 'injury'
  | 'wrongful-death'
  | 'estate'
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
      'Car & truck collisions, 18-wheeler crashes, premises liability, and product liability.',
    detail:
      'The firm’s flagship practice. If you have been hurt because of someone else’s negligence, you deserve straightforward answers and a lawyer who handles your case directly. The firm helps injured people and their families pursue fair compensation for medical bills, lost income, and the disruption an injury causes.',
    points: [
      'Car and truck collisions',
      '18-wheeler and commercial vehicle crashes',
      'Premises liability (unsafe property conditions)',
      'Product liability',
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
      'When a family loses someone because of another’s negligence, the practical and financial questions can feel overwhelming. The firm handles wrongful death matters with care, helping families understand their options and pursue accountability.',
  },
  {
    slug: 'estate-planning',
    title: 'Estate Planning & Wills',
    icon: 'estate',
    blurb: 'Wills and foundational planning to protect your family’s future.',
    detail:
      'Thoughtful planning gives your family clarity and reduces stress later. The firm helps individuals and families put practical documents in place, including wills and related planning, tailored to your situation. Consultations are available; fees are typically flat or hourly depending on the work.',
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
