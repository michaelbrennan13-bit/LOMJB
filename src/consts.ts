/**
 * Site-wide constants for the Law Office of Michael J. Brennan, PLLC.
 *
 * ⚠️  PLACEHOLDERS — edit the values marked "FILL:" before go-live.
 *     Every placeholder is also listed in README.md.
 */

export const SITE = {
  name: 'Law Office of Michael J. Brennan, PLLC',
  shortName: 'Law Office of Michael J. Brennan',
  attorney: 'Michael J. Brennan',
  url: 'https://mjbrennan.com',

  // FILL: firm phone number. Used in header, footer, hero, contact page, and tel: links.
  phone: '(XXX) XXX-XXXX',
  // Digits-only version for the tel: href. FILL to match `phone`.
  phoneHref: '+1XXXXXXXXXX',

  // FILL: contact email address (e.g., michael@mjbrennan.com).
  email: 'CONTACT@mjbrennan.com',

  // Office (virtual / by appointment — do not render a live map pin).
  address: {
    street: '11757 Katy Fwy #1300',
    city: 'Houston',
    region: 'TX',
    postalCode: '77079',
    country: 'US',
  },

  tagline: 'Serving Fort Bend County & Greater Houston.',

  // FILL: office hours, e.g. "By appointment — Mon–Fri 9:00am–5:00pm".
  hours: '[ FILL: office hours ]',

  barNumber: '24125746',

  // FILL: Web3Forms access key from https://web3forms.com (free).
  web3formsKey: '[WEB3FORMS_KEY]',
} as const;

/** Compliance / disclaimer strings — Texas Disciplinary Rules Part VII. */
export const COMPLIANCE = {
  responsible:
    'Michael J. Brennan is responsible for the content of this website. Principal office: Houston, Texas.',
  licensed: `Licensed in Texas — State Bar No. ${SITE.barNumber}.`,
  notLegalAdvice:
    'This website is for general information only and is not legal advice. Contacting the firm or submitting the contact form does not create an attorney-client relationship; please do not send confidential information through it. Past results do not guarantee, warrant, or predict future outcomes.',
  contingencyCosts:
    'Personal injury matters are handled on a contingency-fee basis: you pay no attorney’s fee unless we obtain a recovery for you. Clients may be responsible for court costs and case expenses. [Confirm whether costs are owed regardless of outcome and edit to match your fee agreement.]',
  pastResults:
    'Past results do not guarantee, warrant, or predict future outcomes.',
} as const;

export const NAV = [
  { label: 'Home', href: '/' },
  { label: 'About', href: '/about' },
  { label: 'Practice Areas', href: '/practice-areas' },
  { label: 'Contact', href: '/contact' },
] as const;
