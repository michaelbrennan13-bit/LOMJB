/**
 * Site-wide constants for the Law Office of Michael J. Brennan, PLLC.
 *
 * All site-wide values below are final.
 */

export const SITE = {
  name: 'Law Office of Michael J. Brennan, PLLC',
  shortName: 'Law Office of Michael J. Brennan',
  attorney: 'Michael J. Brennan',
  url: 'https://mjbrennan.com',

  // Firm phone number. Used in header, footer, hero, contact page, and tel: links.
  phone: '(832) 569-7566',
  // Digits-only version for the tel: href.
  phoneHref: '+18325697566',

  email: 'michael@mjbrennan.com',

  // Office (virtual / by appointment — do not render a live map pin).
  address: {
    street: '11757 Katy Fwy #1300',
    city: 'Houston',
    region: 'TX',
    postalCode: '77079',
    country: 'US',
  },

  tagline: 'Serving Fort Bend County & Greater Houston.',

  barNumber: '24125746',

  // Web3Forms access key (https://web3forms.com) — powers the contact form.
  web3formsKey: 'ea9b5e51-61bc-4745-a3e9-4111a12d318f',
} as const;

/** Compliance / disclaimer strings — Texas Disciplinary Rules Part VII. */
export const COMPLIANCE = {
  responsible:
    'Michael J. Brennan is responsible for the content of this website. Principal office: Houston, Texas.',
  licensed: `Licensed in Texas — State Bar No. ${SITE.barNumber}.`,
  notLegalAdvice:
    'This website is for general information only and is not legal advice. Contacting the firm or submitting the contact form does not create an attorney-client relationship; please do not send confidential information through it. Past results do not guarantee, warrant, or predict future outcomes.',
  contingencyCosts:
    'Personal injury matters are handled on a contingency-fee basis: you pay no attorney’s fee unless we obtain a recovery for you. Clients may be responsible for court costs and case expenses.',
  contingencyOptionalNote:
    'Insurance disputes are handled on either a contingency-fee or hourly basis, depending on the matter. When handled on contingency, you pay no attorney’s fee unless we obtain a recovery; court costs and case expenses may still apply. The firm will confirm the fee arrangement in writing before any work begins.',
  pastResults:
    'Past results do not guarantee, warrant, or predict future outcomes.',
  // Condensed single-paragraph disclaimer shown in the site footer (every page).
  footerCondensed:
    'Michael J. Brennan is responsible for this website; principal office in Houston, Texas. Licensed in Texas, State Bar No. 24125746. This site is general information, not legal advice, and using it or submitting the contact form does not create an attorney-client relationship — please do not send confidential information. Personal injury matters are handled on a contingency-fee basis: no attorney’s fee unless we obtain a recovery, though clients may be responsible for court costs and case expenses. Past results do not guarantee, warrant, or predict future outcomes.',
} as const;

export const NAV = [
  { label: 'Home', href: '/' },
  { label: 'About', href: '/about' },
  { label: 'Practice Areas', href: '/practice-areas' },
  { label: 'Contact', href: '/contact' },
] as const;
