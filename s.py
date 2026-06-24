import React, { useState, useMemo } from "react";

/* ---------------------------------------------------------------
   ServiceHub prototype
   Pages: Home, Services Directory, Provider Profile
   Bilingual: English / Hindi (toggle)
   Dark mode toggle
   Signature element: Trust Score ring (ratings + reviews + profile
   completeness + verification, the four inputs named in the brief)
----------------------------------------------------------------- */

const COPY = {
  en: {
    brand: "ServiceHub",
    tagline: "Find people your neighbours already trust",
    searchPlaceholder: "What do you need help with? e.g. electrician, AC repair",
    detectLocation: "Detect my location",
    locationFallback: "Deoria, UP",
    searchBtn: "Search",
    statsProviders: "verified providers",
    statsCities: "cities",
    statsBookings: "bookings this month",
    categoriesTitle: "Browse by category",
    featuredTitle: "Featured providers",
    topRatedTitle: "Top rated this week",
    emergencyTitle: "Need help right now?",
    emergencySub: "Skip the search. These are always one tap away.",
    testimonialsTitle: "What people are saying",
    ctaTitle: "Are you a service provider?",
    ctaSub: "List your business and start receiving bookings from people nearby.",
    ctaBtn: "List your business",
    directoryTitle: "Services directory",
    filterCategory: "Category",
    filterCity: "City",
    filterRating: "Minimum rating",
    sortBy: "Sort by",
    sortPopular: "Most popular",
    sortDistance: "Nearest first",
    sortRating: "Highest rated",
    allCategories: "All categories",
    resultsCount: "providers found",
    viewProfile: "View profile",
    call: "Call",
    whatsapp: "WhatsApp",
    verified: "Verified",
    trustScore: "Trust score",
    backToDirectory: "Back to directory",
    contact: "Contact",
    address: "Address",
    experience: "Experience",
    yearsExp: "years experience",
    servicesOffered: "Services offered",
    workingHours: "Working hours",
    reviews: "Reviews",
    gallery: "Photo gallery",
    bookService: "Book this service",
    selectService: "Select a service",
    selectDate: "Choose date",
    selectTime: "Choose time",
    requestBooking: "Request booking",
    bookingConfirmed: "Booking requested",
    bookingConfirmedSub: "We've sent your request. The provider will confirm shortly.",
    writeReview: "Write a review",
    yourRating: "Your rating",
    yourReview: "Your review",
    submitReview: "Submit review",
    aiAssistant: "Ask ServiceHub AI",
    aiPlaceholder: 'Try: "Find a math tutor near me"',
    aiAsk: "Ask",
    viewOnMap: "View on map",
    openNow: "Open now",
    closed: "Closed now",
    seeAll: "See all",
    homeNav: "Home",
    directoryNav: "Directory",
    emergencyNav: "Emergency",
    langToggle: "हिंदी",
    darkToggle: "Dark",
    lightToggle: "Light",
  },
  hi: {
    brand: "सर्विसहब",
    tagline: "वो लोग खोजें जिन पर आपके पड़ोसी भरोसा करते हैं",
    searchPlaceholder: "आपको किस सेवा की ज़रूरत है? जैसे इलेक्ट्रीशियन, AC रिपेयर",
    detectLocation: "मेरी लोकेशन पहचानें",
    locationFallback: "देवरिया, यूपी",
    searchBtn: "खोजें",
    statsProviders: "सत्यापित प्रदाता",
    statsCities: "शहर",
    statsBookings: "इस महीने की बुकिंग",
    categoriesTitle: "श्रेणी के अनुसार देखें",
    featuredTitle: "विशेष प्रदाता",
    topRatedTitle: "इस सप्ताह के टॉप रेटेड",
    emergencyTitle: "अभी मदद चाहिए?",
    emergencySub: "खोजने की ज़रूरत नहीं। ये हमेशा एक टैप दूर हैं।",
    testimonialsTitle: "लोग क्या कहते हैं",
    ctaTitle: "क्या आप एक सेवा प्रदाता हैं?",
    ctaSub: "अपना बिज़नेस लिस्ट करें और आस-पास के लोगों से बुकिंग पाएं।",
    ctaBtn: "अपना बिज़नेस लिस्ट करें",
    directoryTitle: "सेवा निर्देशिका",
    filterCategory: "श्रेणी",
    filterCity: "शहर",
    filterRating: "न्यूनतम रेटिंग",
    sortBy: "क्रमबद्ध करें",
    sortPopular: "सबसे लोकप्रिय",
    sortDistance: "नज़दीकी पहले",
    sortRating: "सर्वोच्च रेटेड",
    allCategories: "सभी श्रेणियाँ",
    resultsCount: "प्रदाता मिले",
    viewProfile: "प्रोफ़ाइल देखें",
    call: "कॉल करें",
    whatsapp: "व्हाट्सऐप",
    verified: "सत्यापित",
    trustScore: "ट्रस्ट स्कोर",
    backToDirectory: "निर्देशिका पर वापस जाएं",
    contact: "संपर्क",
    address: "पता",
    experience: "अनुभव",
    yearsExp: "वर्षों का अनुभव",
    servicesOffered: "सेवाएं",
    workingHours: "कार्य समय",
    reviews: "रिव्यू",
    gallery: "फोटो गैलरी",
    bookService: "सेवा बुक करें",
    selectService: "सेवा चुनें",
    selectDate: "तारीख चुनें",
    selectTime: "समय चुनें",
    requestBooking: "बुकिंग का अनुरोध करें",
    bookingConfirmed: "बुकिंग का अनुरोध भेजा गया",
    bookingConfirmedSub: "हमने आपका अनुरोध भेज दिया है। प्रदाता शीघ्र पुष्टि करेंगे।",
    writeReview: "रिव्यू लिखें",
    yourRating: "आपकी रेटिंग",
    yourReview: "आपका रिव्यू",
    submitReview: "रिव्यू सबमिट करें",
    aiAssistant: "सर्विसहब AI से पूछें",
    aiPlaceholder: 'जैसे: "मेरे पास गणित ट्यूटर खोजें"',
    aiAsk: "पूछें",
    viewOnMap: "मैप पर देखें",
    openNow: "अभी खुला है",
    closed: "अभी बंद है",
    seeAll: "सभी देखें",
    homeNav: "होम",
    directoryNav: "निर्देशिका",
    emergencyNav: "इमरजेंसी",
    langToggle: "English",
    darkToggle: "डार्क",
    lightToggle: "लाइट",
  },
};

const CATEGORIES = [
  { id: "electrician", en: "Electrician", hi: "इलेक्ट्रीशियन", icon: "bolt" },
  { id: "plumber", en: "Plumber", hi: "प्लंबर", icon: "droplet" },
  { id: "mechanic", en: "Mechanic", hi: "मैकेनिक", icon: "car" },
  { id: "tutor", en: "Tutor", hi: "ट्यूटर", icon: "book" },
  { id: "hospital", en: "Hospital", hi: "हॉस्पिटल", icon: "cross" },
  { id: "carpenter", en: "Carpenter", hi: "कारपेंटर", icon: "hammer" },
  { id: "ac_repair", en: "AC repair", hi: "AC रिपेयर", icon: "snowflake" },
  { id: "mobile_repair", en: "Mobile repair", hi: "मोबाइल रिपेयर", icon: "phone" },
];

const PROVIDERS = [
  {
    id: 1,
    name: "Rajesh Kumar Electricals",
    nameHi: "राजेश कुमार इलेक्ट्रिकल्स",
    category: "electrician",
    city: "Deoria",
    rating: 4.8,
    reviewCount: 142,
    verified: true,
    completeness: 95,
    responseRate: 92,
    experience: 12,
    distanceKm: 1.2,
    phone: "+91 98765 43210",
    address: "Civil Lines, Deoria, UP 274001",
    hours: "8:00 AM - 9:00 PM",
    openNow: true,
    services: ["Wiring repair", "Switchboard install", "Fan & light fitting", "Inverter setup"],
    bio: "12 years fixing homes and shops across Deoria. Same-day service for urgent jobs.",
    color: "#1B4F72",
  },
  {
    id: 2,
    name: "Sharma Plumbing Works",
    nameHi: "शर्मा प्लंबिंग वर्क्स",
    category: "plumber",
    city: "Deoria",
    rating: 4.6,
    reviewCount: 98,
    verified: true,
    completeness: 88,
    responseRate: 85,
    experience: 8,
    distanceKm: 2.4,
    phone: "+91 98765 11223",
    address: "Gorakhpur Road, Deoria, UP 274001",
    hours: "7:00 AM - 8:00 PM",
    openNow: true,
    services: ["Leak repair", "Bathroom fitting", "Pipeline install", "Tank cleaning"],
    bio: "Family-run plumbing business serving Deoria since 2016.",
    color: "#2E8B57",
  },
  {
    id: 3,
    name: "Singh Auto Care",
    nameHi: "सिंह ऑटो केयर",
    category: "mechanic",
    city: "Deoria",
    rating: 4.3,
    reviewCount: 64,
    verified: false,
    completeness: 60,
    responseRate: 70,
    experience: 6,
    distanceKm: 3.1,
    phone: "+91 98765 99887",
    address: "Station Road, Deoria, UP 274001",
    hours: "9:00 AM - 7:00 PM",
    openNow: false,
    services: ["Bike servicing", "Car AC repair", "Battery replacement", "Engine diagnostics"],
    bio: "Quick and honest diagnostics for bikes and cars.",
    color: "#1B4F72",
  },
  {
    id: 4,
    name: "Priya Mishra Maths Tuition",
    nameHi: "प्रिया मिश्रा मैथ्स ट्यूशन",
    category: "tutor",
    city: "Deoria",
    rating: 4.9,
    reviewCount: 211,
    verified: true,
    completeness: 100,
    responseRate: 97,
    experience: 9,
    distanceKm: 0.8,
    phone: "+91 98765 33445",
    address: "Kasya Road, Deoria, UP 274001",
    hours: "3:00 PM - 8:00 PM",
    openNow: true,
    services: ["Class 9-10 Maths", "Class 11-12 Maths", "Olympiad prep", "Online classes"],
    bio: "9 years teaching maths to classes 9 through 12, board exam focused.",
    color: "#2E8B57",
  },
  {
    id: 5,
    name: "City Care Hospital",
    nameHi: "सिटी केयर हॉस्पिटल",
    category: "hospital",
    city: "Deoria",
    rating: 4.5,
    reviewCount: 320,
    verified: true,
    completeness: 90,
    responseRate: 99,
    experience: 20,
    distanceKm: 4.5,
    phone: "+91 98765 00111",
    address: "Hospital Road, Deoria, UP 274001",
    hours: "Open 24 hours",
    openNow: true,
    services: ["Emergency care", "General medicine", "Pediatrics", "Diagnostics lab"],
    bio: "Multi-speciality hospital with 24-hour emergency services.",
    color: "#D97706",
  },
  {
    id: 6,
    name: "Bharat AC Solutions",
    nameHi: "भारत AC सॉल्यूशंस",
    category: "ac_repair",
    city: "Deoria",
    rating: 4.4,
    reviewCount: 76,
    verified: true,
    completeness: 80,
    responseRate: 88,
    experience: 5,
    distanceKm: 2.9,
    phone: "+91 98765 22556",
    address: "Bypass Road, Deoria, UP 274001",
    hours: "8:00 AM - 9:00 PM",
    openNow: true,
    services: ["AC servicing", "Gas refill", "Installation", "Annual maintenance"],
    bio: "Fast AC repair, especially during peak summer load.",
    color: "#1B4F72",
  },
];

const TESTIMONIALS = [
  {
    en: "Found an electrician within ten minutes during a power cut. He showed up the same evening.",
    hi: "बिजली कटने के दौरान दस मिनट में इलेक्ट्रीशियन मिल गया। वह उस शाम ही आ गए।",
    name: "Anita S.",
  },
  {
    en: "The trust score actually means something — picked the highest one and had zero issues.",
    hi: "ट्रस्ट स्कोर वाकई काम का है — सबसे ज़्यादा वाला चुना और कोई परेशानी नहीं हुई।",
    name: "Vikram T.",
  },
  {
    en: "My daughter's maths tutor was booked through ServiceHub. Two years now, never looked back.",
    hi: "मेरी बेटी की मैथ्स ट्यूटर सर्विसहब से बुक हुई थी। दो साल हो गए, कभी पीछे नहीं देखा।",
    name: "Rekha M.",
  },
];

const REVIEWS = [
  { name: "Amit J.", rating: 5, en: "Came within 30 minutes, fixed the short circuit fast.", hi: "30 मिनट में आ गए, शॉर्ट सर्किट जल्दी ठीक कर दिया।" },
  { name: "Sunita P.", rating: 4, en: "Good work but arrived a bit late.", hi: "काम अच्छा था लेकिन थोड़ी देर से आए।" },
  { name: "Manoj R.", rating: 5, en: "Fair pricing, explained everything clearly.", hi: "उचित दाम, सब कुछ साफ़ समझाया।" },
];

function trustScore(p) {
  const ratingPart = (p.rating / 5) * 40;
  const reviewPart = Math.min(p.reviewCount / 200, 1) * 20;
  const completenessPart = (p.completeness / 100) * 20;
  const verifiedPart = p.verified ? 15 : 0;
  const responsePart = (p.responseRate / 100) * 5;
  return Math.round(ratingPart + reviewPart + completenessPart + verifiedPart + responsePart);
}

function TrustRing({ score, size = 56, theme }) {
  const radius = (size - 8) / 2;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (score / 100) * circumference;
  const color = score >= 80 ? "#2E8B57" : score >= 60 ? "#D97706" : "#B91C1C";
  return (
    <div style={{ position: "relative", width: size, height: size }}>
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke={theme === "dark" ? "#27374a" : "#E5E9EF"}
          strokeWidth="4"
        />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke={color}
          strokeWidth="4"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          strokeLinecap="round"
          transform={`rotate(-90 ${size / 2} ${size / 2})`}
          style={{ transition: "stroke-dashoffset 0.6s ease" }}
        />
      </svg>
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          width: size,
          height: size,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <span style={{ fontSize: size > 48 ? 15 : 12, fontWeight: 700, color: theme === "dark" ? "#F5F7FA" : "#1B2733" }}>
          {score}
        </span>
      </div>
    </div>
  );
}

function Icon({ name, size = 20, color = "currentColor" }) {
  const paths = {
    bolt: "M13 2L4 14h6l-1 8 9-12h-6l1-8z",
    droplet: "M12 2s7 8 7 13a7 7 0 11-14 0c0-5 7-13 7-13z",
    car: "M5 17h14M6 17a2 2 0 11-4 0 2 2 0 014 0zM20 17a2 2 0 11-4 0 2 2 0 014 0zM3 17V12l2-5h14l2 5v5",
    book: "M4 4h11a3 3 0 013 3v13H7a3 3 0 01-3-3V4zM4 4v13a3 3 0 003 3h11",
    cross: "M12 4v16M4 12h16",
    hammer: "M14 6l5 5-2 2-5-5 2-2zM3 21l8-8M11 9l2-2 4 4-2 2-4-4z",
    snowflake: "M12 2v20M5 7l14 10M19 7L5 17M2 12h20",
    phone: "M7 2h10a2 2 0 012 2v16a2 2 0 01-2 2H7a2 2 0 01-2-2V4a2 2 0 012-2zM11 18h2",
    search: "M11 4a7 7 0 100 14 7 7 0 000-14zM21 21l-4.3-4.3",
    location: "M12 2a7 7 0 00-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 00-7-7zM12 12a2 2 0 100-4 2 2 0 000 4z",
    star: "M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z",
    check: "M20 6L9 17l-5-5",
    whatsapp: "M12 2a10 10 0 00-8.5 15.3L2 22l4.9-1.3A10 10 0 1012 2z",
    phoneCall: "M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z",
    map: "M9 20l-5-2V4l5 2 6-2 5 2v14l-5-2-6 2zM9 6v14M15 4v14",
    sun: "M12 17a5 5 0 100-10 5 5 0 000 10zM12 1v3M12 20v3M4.2 4.2l2 2M17.8 17.8l2 2M1 12h3M20 12h3M4.2 19.8l2-2M17.8 6.2l2-2",
    moon: "M21 12.8A9 9 0 1111.2 3 7 7 0 0021 12.8z",
    back: "M19 12H5M12 19l-7-7 7-7",
  };
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d={paths[name] || paths.star} />
    </svg>
  );
}

function Stars({ rating, size = 14 }) {
  return (
    <div style={{ display: "flex", gap: 2 }}>
      {[1, 2, 3, 4, 5].map((i) => (
        <Icon key={i} name="star" size={size} color={i <= Math.round(rating) ? "#D97706" : "#C8CDD3"} />
      ))}
    </div>
  );
}

export default function ServiceHub() {
  const [lang, setLang] = useState("en");
  const [theme, setTheme] = useState("light");
  const [page, setPage] = useState("home");
  const [selectedProviderId, setSelectedProviderId] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");
  const [filterCategory, setFilterCategory] = useState("all");
  const [filterRating, setFilterRating] = useState(0);
  const [sortBy, setSortBy] = useState("popular");
  const [aiQuery, setAiQuery] = useState("");
  const [aiResult, setAiResult] = useState(null);
  const [bookingStep, setBookingStep] = useState(null);
  const [bookingDone, setBookingDone] = useState(false);

  const t = COPY[lang];
  const isDark = theme === "dark";

  const colors = {
    bg: isDark ? "#0F1A24" : "#FAFAF7",
    surface: isDark ? "#16232F" : "#FFFFFF",
    surfaceAlt: isDark ? "#1C2A38" : "#F1F4F8",
    border: isDark ? "#27374a" : "#E5E9EF",
    text: isDark ? "#F5F7FA" : "#1B2733",
    textMuted: isDark ? "#9AAAB8" : "#5B6878",
    primary: "#1B4F72",
    primaryLight: isDark ? "#2C6794" : "#1B4F72",
    accent: "#2E8B57",
    urgent: "#D97706",
  };

  const navigate = (p, providerId = null) => {
    setPage(p);
    if (providerId) setSelectedProviderId(providerId);
    setBookingStep(null);
    setBookingDone(false);
  };

  const filteredProviders = useMemo(() => {
    let list = PROVIDERS.filter((p) => {
      const matchesCategory = filterCategory === "all" || p.category === filterCategory;
      const matchesRating = p.rating >= filterRating;
      const matchesSearch =
        !searchTerm ||
        p.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        p.category.includes(searchTerm.toLowerCase()) ||
        CATEGORIES.find((c) => c.id === p.category)?.en.toLowerCase().includes(searchTerm.toLowerCase());
      return matchesCategory && matchesRating && matchesSearch;
    });
    if (sortBy === "rating") list = [...list].sort((a, b) => b.rating - a.rating);
    else if (sortBy === "distance") list = [...list].sort((a, b) => a.distanceKm - b.distanceKm);
    else list = [...list].sort((a, b) => b.reviewCount - a.reviewCount);
    return list;
  }, [filterCategory, filterRating, searchTerm, sortBy]);

  const selectedProvider = PROVIDERS.find((p) => p.id === selectedProviderId);

  const handleAiAsk = () => {
    const q = aiQuery.toLowerCase();
    let match = CATEGORIES.find((c) => q.includes(c.en.toLowerCase()) || q.includes(c.id));
    if (!q.trim()) return;
    let results = PROVIDERS;
    if (match) results = results.filter((p) => p.category === match.id);
    if (q.includes("highest") || q.includes("best") || q.includes("top")) {
      results = [...results].sort((a, b) => b.rating - a.rating);
    }
    setAiResult(results.slice(0, 3));
  };

  const cardStyle = {
    background: colors.surface,
    border: `1px solid ${colors.border}`,
    borderRadius: 16,
    padding: 20,
  };

  const buttonPrimary = {
    background: colors.primary,
    color: "#fff",
    border: "none",
    borderRadius: 10,
    padding: "12px 20px",
    fontWeight: 600,
    fontSize: 14,
    cursor: "pointer",
  };

  const buttonOutline = {
    background: "transparent",
    color: colors.text,
    border: `1px solid ${colors.border}`,
    borderRadius: 10,
    padding: "10px 16px",
    fontWeight: 500,
    fontSize: 13,
    cursor: "pointer",
  };

  /* ---------------- NAVBAR ---------------- */
  const Navbar = () => (
    <div
      style={{
        position: "sticky",
        top: 0,
        zIndex: 50,
        background: colors.surface,
        borderBottom: `1px solid ${colors.border}`,
        padding: "14px 24px",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        flexWrap: "wrap",
        gap: 12,
      }}
    >
      <div
        onClick={() => navigate("home")}
        style={{ display: "flex", alignItems: "center", gap: 8, cursor: "pointer", fontWeight: 700, fontSize: 18, color: colors.text }}
      >
        <div style={{ width: 30, height: 30, borderRadius: 8, background: colors.primary, display: "flex", alignItems: "center", justifyContent: "center" }}>
          <Icon name="bolt" size={16} color="#fff" />
        </div>
        {t.brand}
      </div>
      <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
        <button onClick={() => navigate("home")} style={{ ...buttonOutline, border: "none", color: page === "home" ? colors.primary : colors.textMuted }}>
          {t.homeNav}
        </button>
        <button onClick={() => navigate("directory")} style={{ ...buttonOutline, border: "none", color: page === "directory" ? colors.primary : colors.textMuted }}>
          {t.directoryNav}
        </button>
        <button onClick={() => navigate("emergency")} style={{ ...buttonOutline, border: "none", color: page === "emergency" ? colors.urgent : colors.textMuted }}>
          {t.emergencyNav}
        </button>
        <div style={{ width: 1, height: 20, background: colors.border, margin: "0 4px" }} />
        <button onClick={() => setLang(lang === "en" ? "hi" : "en")} style={buttonOutline}>
          {t.langToggle}
        </button>
        <button onClick={() => setTheme(isDark ? "light" : "dark")} style={{ ...buttonOutline, display: "flex", alignItems: "center", gap: 6 }}>
          <Icon name={isDark ? "sun" : "moon"} size={14} />
          {isDark ? t.lightToggle : t.darkToggle}
        </button>
      </div>
    </div>
  );

  /* ---------------- PROVIDER CARD ---------------- */
  const ProviderCard = ({ p, compact }) => {
    const score = trustScore(p);
    const cat = CATEGORIES.find((c) => c.id === p.category);
    return (
      <div style={{ ...cardStyle, display: "flex", flexDirection: "column", gap: 14 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
          <div style={{ display: "flex", gap: 12 }}>
            <div
              style={{
                width: 52,
                height: 52,
                borderRadius: 12,
                background: p.color,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                color: "#fff",
                fontWeight: 700,
                fontSize: 18,
                flexShrink: 0,
              }}
            >
              {(lang === "hi" ? p.nameHi : p.name).charAt(0)}
            </div>
            <div>
              <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
                <span style={{ fontWeight: 700, fontSize: 15, color: colors.text }}>{lang === "hi" ? p.nameHi : p.name}</span>
                {p.verified && (
                  <span title={t.verified} style={{ color: colors.accent, display: "flex" }}>
                    <Icon name="check" size={14} color={colors.accent} />
                  </span>
                )}
              </div>
              <div style={{ fontSize: 13, color: colors.textMuted, marginTop: 2 }}>
                {lang === "hi" ? cat?.hi : cat?.en} &middot; {p.city} &middot; {p.distanceKm} km
              </div>
              <div style={{ display: "flex", alignItems: "center", gap: 6, marginTop: 6 }}>
                <Stars rating={p.rating} />
                <span style={{ fontSize: 13, color: colors.textMuted }}>
                  {p.rating} ({p.reviewCount})
                </span>
              </div>
            </div>
          </div>
          <TrustRing score={score} size={48} theme={theme} />
        </div>
        {!compact && <div style={{ fontSize: 13, color: colors.textMuted, lineHeight: 1.5 }}>{p.bio}</div>}
        <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
          <button style={{ ...buttonPrimary, flex: 1, padding: "10px 14px", fontSize: 13 }} onClick={() => navigate("profile", p.id)}>
            {t.viewProfile}
          </button>
          <a href={`tel:${p.phone}`} style={{ ...buttonOutline, display: "flex", alignItems: "center", gap: 6, textDecoration: "none" }}>
            <Icon name="phoneCall" size={14} />
          </a>
          <a
            href={`https://wa.me/${p.phone.replace(/\D/g, "")}`}
            target="_blank"
            rel="noopener noreferrer"
            style={{ ...buttonOutline, display: "flex", alignItems: "center", gap: 6, color: colors.accent, textDecoration: "none" }}
          >
            <Icon name="whatsapp" size={14} color={colors.accent} />
          </a>
        </div>
      </div>
    );
  };

  /* ---------------- HOME PAGE ---------------- */
  const HomePage = () => (
    <div>
      <div
        style={{
          background: isDark ? "linear-gradient(180deg, #16232F 0%, #0F1A24 100%)" : "linear-gradient(180deg, #EFF6FF 0%, #FAFAF7 100%)",
          padding: "56px 24px 64px",
          textAlign: "center",
        }}
      >
        <h1 style={{ fontSize: 36, fontWeight: 800, color: colors.text, margin: "0 0 10px", maxWidth: 600, marginLeft: "auto", marginRight: "auto" }}>
          {t.tagline}
        </h1>
        <div style={{ maxWidth: 600, margin: "28px auto 0", display: "flex", flexDirection: "column", gap: 10 }}>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 10,
              background: colors.surface,
              border: `1px solid ${colors.border}`,
              borderRadius: 14,
              padding: "6px 8px 6px 16px",
              boxShadow: isDark ? "none" : "0 4px 20px rgba(27,79,114,0.08)",
            }}
          >
            <Icon name="search" size={18} color={colors.textMuted} />
            <input
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder={t.searchPlaceholder}
              style={{
                flex: 1,
                border: "none",
                outline: "none",
                background: "transparent",
                fontSize: 14,
                padding: "10px 0",
                color: colors.text,
              }}
            />
            <button style={buttonPrimary} onClick={() => navigate("directory")}>
              {t.searchBtn}
            </button>
          </div>
          <button
            onClick={() => {}}
            style={{
              alignSelf: "center",
              display: "flex",
              alignItems: "center",
              gap: 6,
              background: "none",
              border: "none",
              color: colors.primary,
              fontSize: 13,
              fontWeight: 600,
              cursor: "pointer",
            }}
          >
            <Icon name="location" size={14} color={colors.primary} />
            {t.detectLocation} ({t.locationFallback})
          </button>
        </div>
        <div style={{ display: "flex", justifyContent: "center", gap: 32, marginTop: 36, flexWrap: "wrap" }}>
          {[
            ["12,400+", t.statsProviders],
            ["38", t.statsCities],
            ["3,210", t.statsBookings],
          ].map(([num, label]) => (
            <div key={label}>
              <div style={{ fontSize: 24, fontWeight: 800, color: colors.primary }}>{num}</div>
              <div style={{ fontSize: 12, color: colors.textMuted }}>{label}</div>
            </div>
          ))}
        </div>
      </div>

      <Section title={t.categoriesTitle}>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(120px, 1fr))", gap: 14 }}>
          {CATEGORIES.map((c) => (
            <div
              key={c.id}
              onClick={() => {
                setFilterCategory(c.id);
                navigate("directory");
              }}
              style={{
                ...cardStyle,
                padding: 16,
                textAlign: "center",
                cursor: "pointer",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                gap: 8,
              }}
            >
              <div
                style={{
                  width: 44,
                  height: 44,
                  borderRadius: 12,
                  background: colors.surfaceAlt,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                }}
              >
                <Icon name={c.icon} size={20} color={colors.primary} />
              </div>
              <span style={{ fontSize: 13, fontWeight: 600, color: colors.text }}>{lang === "hi" ? c.hi : c.en}</span>
            </div>
          ))}
        </div>
      </Section>

      <Section title={t.aiAssistant}>
        <div style={{ ...cardStyle, maxWidth: 700, margin: "0 auto" }}>
          <div style={{ display: "flex", gap: 10 }}>
            <input
              value={aiQuery}
              onChange={(e) => setAiQuery(e.target.value)}
              placeholder={t.aiPlaceholder}
              style={{
                flex: 1,
                border: `1px solid ${colors.border}`,
                borderRadius: 10,
                padding: "10px 14px",
                fontSize: 14,
                background: colors.surfaceAlt,
                color: colors.text,
                outline: "none",
              }}
              onKeyDown={(e) => e.key === "Enter" && handleAiAsk()}
            />
            <button style={buttonPrimary} onClick={handleAiAsk}>
              {t.aiAsk}
            </button>
          </div>
          {aiResult && (
            <div style={{ marginTop: 16, display: "grid", gap: 10 }}>
              {aiResult.length === 0 ? (
                <div style={{ fontSize: 13, color: colors.textMuted }}>
                  {lang === "hi" ? "कोई मिलान नहीं मिला।" : "No matches found."}
                </div>
              ) : (
                aiResult.map((p) => (
                  <div
                    key={p.id}
                    onClick={() => navigate("profile", p.id)}
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      alignItems: "center",
                      padding: "10px 14px",
                      borderRadius: 10,
                      background: colors.surfaceAlt,
                      cursor: "pointer",
                    }}
                  >
                    <div>
                      <div style={{ fontWeight: 600, fontSize: 13, color: colors.text }}>{lang === "hi" ? p.nameHi : p.name}</div>
                      <div style={{ fontSize: 12, color: colors.textMuted }}>
                        {p.rating} <Icon name="star" size={11} color={colors.urgent} /> &middot; {p.distanceKm} km
                      </div>
                    </div>
                    <TrustRing score={trustScore(p)} size={36} theme={theme} />
                  </div>
                ))
              )}
            </div>
          )}
        </div>
      </Section>

      <Section title={t.featuredTitle}>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 16 }}>
          {PROVIDERS.slice(0, 3).map((p) => (
            <ProviderCard key={p.id} p={p} />
          ))}
        </div>
      </Section>

      <Section title={t.topRatedTitle}>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 16 }}>
          {[...PROVIDERS]
            .sort((a, b) => b.rating - a.rating)
            .slice(0, 3)
            .map((p) => (
              <ProviderCard key={p.id} p={p} compact />
            ))}
        </div>
      </Section>

      <div style={{ padding: "8px 24px 48px" }}>
        <div
          style={{
            background: isDark ? "#2A1B0E" : "#FFF7ED",
            border: `1px solid ${colors.urgent}33`,
            borderRadius: 16,
            padding: 24,
            maxWidth: 1100,
            margin: "0 auto",
          }}
        >
          <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 4 }}>
            <Icon name="cross" size={18} color={colors.urgent} />
            <h3 style={{ fontSize: 17, fontWeight: 700, color: colors.text, margin: 0 }}>{t.emergencyTitle}</h3>
          </div>
          <p style={{ fontSize: 13, color: colors.textMuted, margin: "4px 0 16px" }}>{t.emergencySub}</p>
          <button style={{ ...buttonPrimary, background: colors.urgent }} onClick={() => navigate("emergency")}>
            {t.emergencyNav}
          </button>
        </div>
      </div>

      <Section title={t.testimonialsTitle}>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 16 }}>
          {TESTIMONIALS.map((tm, i) => (
            <div key={i} style={cardStyle}>
              <Stars rating={5} />
              <p style={{ fontSize: 13, color: colors.text, lineHeight: 1.6, margin: "10px 0" }}>
                {lang === "hi" ? tm.hi : tm.en}
              </p>
              <span style={{ fontSize: 12, color: colors.textMuted, fontWeight: 600 }}>{tm.name}</span>
            </div>
          ))}
        </div>
      </Section>

      <div style={{ padding: "8px 24px 64px" }}>
        <div
          style={{
            background: colors.primary,
            borderRadius: 20,
            padding: 36,
            textAlign: "center",
            maxWidth: 1100,
            margin: "0 auto",
          }}
        >
          <h3 style={{ color: "#fff", fontSize: 22, fontWeight: 800, margin: "0 0 8px" }}>{t.ctaTitle}</h3>
          <p style={{ color: "#D6E4F0", fontSize: 14, margin: "0 0 20px" }}>{t.ctaSub}</p>
          <button style={{ ...buttonPrimary, background: "#fff", color: colors.primary }}>{t.ctaBtn}</button>
        </div>
      </div>
    </div>
  );

  const Section = ({ title, children }) => (
    <div style={{ padding: "40px 24px", maxWidth: 1100, margin: "0 auto" }}>
      <h2 style={{ fontSize: 20, fontWeight: 700, color: colors.text, margin: "0 0 20px" }}>{title}</h2>
      {children}
    </div>
  );

  /* ---------------- DIRECTORY PAGE ---------------- */
  const DirectoryPage = () => (
    <div style={{ maxWidth: 1100, margin: "0 auto", padding: "32px 24px" }}>
      <h1 style={{ fontSize: 24, fontWeight: 800, color: colors.text, margin: "0 0 20px" }}>{t.directoryTitle}</h1>

      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 10,
          background: colors.surface,
          border: `1px solid ${colors.border}`,
          borderRadius: 12,
          padding: "8px 14px",
          marginBottom: 20,
        }}
      >
        <Icon name="search" size={16} color={colors.textMuted} />
        <input
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder={t.searchPlaceholder}
          style={{ flex: 1, border: "none", outline: "none", background: "transparent", fontSize: 14, padding: "8px 0", color: colors.text }}
        />
      </div>

      <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginBottom: 24 }}>
        <select
          value={filterCategory}
          onChange={(e) => setFilterCategory(e.target.value)}
          style={selectStyle(colors)}
        >
          <option value="all">{t.allCategories}</option>
          {CATEGORIES.map((c) => (
            <option key={c.id} value={c.id}>
              {lang === "hi" ? c.hi : c.en}
            </option>
          ))}
        </select>
        <select value={filterRating} onChange={(e) => setFilterRating(Number(e.target.value))} style={selectStyle(colors)}>
          <option value={0}>{t.filterRating}</option>
          <option value={4.5}>4.5+</option>
          <option value={4}>4.0+</option>
          <option value={3}>3.0+</option>
        </select>
        <select value={sortBy} onChange={(e) => setSortBy(e.target.value)} style={selectStyle(colors)}>
          <option value="popular">{t.sortPopular}</option>
          <option value="distance">{t.sortDistance}</option>
          <option value="rating">{t.sortRating}</option>
        </select>
      </div>

      <div style={{ fontSize: 13, color: colors.textMuted, marginBottom: 16 }}>
        {filteredProviders.length} {t.resultsCount}
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 16 }}>
        {filteredProviders.map((p) => (
          <ProviderCard key={p.id} p={p} />
        ))}
      </div>
      {filteredProviders.length === 0 && (
        <div style={{ textAlign: "center", padding: 60, color: colors.textMuted, fontSize: 14 }}>
          {lang === "hi" ? "इस फ़िल्टर से कोई प्रदाता नहीं मिला।" : "No providers match these filters."}
        </div>
      )}
    </div>
  );

  /* ---------------- PROVIDER PROFILE PAGE ---------------- */
  const ProfilePage = () => {
    if (!selectedProvider) return null;
    const p = selectedProvider;
    const score = trustScore(p);
    const cat = CATEGORIES.find((c) => c.id === p.category);
    const [bookService, setBookService] = useState(p.services[0]);
    const [bookDate, setBookDate] = useState("");
    const [bookTime, setBookTime] = useState("");
    const [reviewRating, setReviewRating] = useState(5);
    const [reviewText, setReviewText] = useState("");
    const [reviewSubmitted, setReviewSubmitted] = useState(false);

    return (
      <div style={{ maxWidth: 900, margin: "0 auto", padding: "28px 24px 64px" }}>
        <button
          onClick={() => navigate("directory")}
          style={{ display: "flex", alignItems: "center", gap: 6, background: "none", border: "none", color: colors.textMuted, fontSize: 13, cursor: "pointer", marginBottom: 20, padding: 0 }}
        >
          <Icon name="back" size={14} />
          {t.backToDirectory}
        </button>

        <div style={{ ...cardStyle, display: "flex", flexWrap: "wrap", gap: 20, alignItems: "flex-start" }}>
          <div
            style={{
              width: 80,
              height: 80,
              borderRadius: 16,
              background: p.color,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "#fff",
              fontWeight: 700,
              fontSize: 28,
              flexShrink: 0,
            }}
          >
            {(lang === "hi" ? p.nameHi : p.name).charAt(0)}
          </div>
          <div style={{ flex: 1, minWidth: 200 }}>
            <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
              <h1 style={{ fontSize: 22, fontWeight: 800, color: colors.text, margin: 0 }}>{lang === "hi" ? p.nameHi : p.name}</h1>
              {p.verified && (
                <span
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 4,
                    background: `${colors.accent}1A`,
                    color: colors.accent,
                    fontSize: 11,
                    fontWeight: 700,
                    padding: "3px 8px",
                    borderRadius: 6,
                  }}
                >
                  <Icon name="check" size={11} color={colors.accent} />
                  {t.verified}
                </span>
              )}
            </div>
            <div style={{ fontSize: 13, color: colors.textMuted, margin: "4px 0 8px" }}>
              {lang === "hi" ? cat?.hi : cat?.en} &middot; {p.city}
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
              <Stars rating={p.rating} size={15} />
              <span style={{ fontSize: 13, color: colors.text, fontWeight: 600 }}>{p.rating}</span>
              <span style={{ fontSize: 13, color: colors.textMuted }}>({p.reviewCount} {t.reviews.toLowerCase()})</span>
            </div>
            <p style={{ fontSize: 13, color: colors.textMuted, lineHeight: 1.6, marginTop: 12 }}>{p.bio}</p>
          </div>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 6 }}>
            <TrustRing score={score} size={72} theme={theme} />
            <span style={{ fontSize: 11, color: colors.textMuted, fontWeight: 600 }}>{t.trustScore}</span>
          </div>
        </div>

        <div style={{ display: "flex", gap: 10, marginTop: 16, flexWrap: "wrap" }}>
          <a href={`tel:${p.phone}`} style={{ ...buttonPrimary, display: "flex", alignItems: "center", gap: 6, textDecoration: "none" }}>
            <Icon name="phoneCall" size={14} color="#fff" />
            {t.call}
          </a>
          <a
            href={`https://wa.me/${p.phone.replace(/\D/g, "")}`}
            target="_blank"
            rel="noopener noreferrer"
            style={{ ...buttonOutline, display: "flex", alignItems: "center", gap: 6, color: colors.accent, borderColor: colors.accent, textDecoration: "none" }}
          >
            <Icon name="whatsapp" size={14} color={colors.accent} />
            {t.whatsapp}
          </a>
          <button style={buttonOutline} onClick={() => navigate("emergency")}>
            <span style={{ display: "flex", alignItems: "center", gap: 6 }}>
              <Icon name="map" size={14} />
              {t.viewOnMap}
            </span>
          </button>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))", gap: 16, marginTop: 28 }}>
          <InfoCard icon="location" label={t.address} value={p.address} colors={colors} />
          <InfoCard icon="bolt" label={t.experience} value={`${p.experience} ${t.yearsExp}`} colors={colors} />
          <InfoCard
            icon="check"
            label={t.workingHours}
            value={p.hours}
            badge={p.openNow ? t.openNow : t.closed}
            badgeColor={p.openNow ? colors.accent : "#B91C1C"}
            colors={colors}
          />
        </div>

        <Section title={t.servicesOffered}>
          <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
            {p.services.map((s) => (
              <span
                key={s}
                style={{
                  background: colors.surfaceAlt,
                  color: colors.text,
                  fontSize: 13,
                  fontWeight: 500,
                  padding: "8px 14px",
                  borderRadius: 10,
                }}
              >
                {s}
              </span>
            ))}
          </div>
        </Section>

        <Section title={t.gallery}>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(140px, 1fr))", gap: 10 }}>
            {[1, 2, 3, 4].map((i) => (
              <div
                key={i}
                style={{
                  height: 110,
                  borderRadius: 12,
                  background: colors.surfaceAlt,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  color: colors.textMuted,
                  fontSize: 12,
                }}
              >
                {lang === "hi" ? "फोटो" : "Photo"} {i}
              </div>
            ))}
          </div>
        </Section>

        <Section title={t.bookService}>
          {!bookingDone ? (
            <div style={cardStyle}>
              <Field label={t.selectService} colors={colors}>
                <select value={bookService} onChange={(e) => setBookService(e.target.value)} style={{ ...selectStyle(colors), width: "100%" }}>
                  {p.services.map((s) => (
                    <option key={s} value={s}>
                      {s}
                    </option>
                  ))}
                </select>
              </Field>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12, marginTop: 14 }}>
                <Field label={t.selectDate} colors={colors}>
                  <input type="date" value={bookDate} onChange={(e) => setBookDate(e.target.value)} style={{ ...selectStyle(colors), width: "100%" }} />
                </Field>
                <Field label={t.selectTime} colors={colors}>
                  <input type="time" value={bookTime} onChange={(e) => setBookTime(e.target.value)} style={{ ...selectStyle(colors), width: "100%" }} />
                </Field>
              </div>
              <button
                style={{ ...buttonPrimary, marginTop: 18, width: "100%" }}
                onClick={() => setBookingDone(true)}
                disabled={!bookDate || !bookTime}
              >
                {t.requestBooking}
              </button>
            </div>
          ) : (
            <div style={{ ...cardStyle, textAlign: "center", borderColor: colors.accent }}>
              <div
                style={{
                  width: 48,
                  height: 48,
                  borderRadius: "50%",
                  background: `${colors.accent}1A`,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  margin: "0 auto 12px",
                }}
              >
                <Icon name="check" size={22} color={colors.accent} />
              </div>
              <h3 style={{ fontSize: 16, fontWeight: 700, color: colors.text, margin: "0 0 6px" }}>{t.bookingConfirmed}</h3>
              <p style={{ fontSize: 13, color: colors.textMuted, margin: 0 }}>{t.bookingConfirmedSub}</p>
            </div>
          )}
        </Section>

        <Section title={t.reviews}>
          <div style={{ display: "grid", gap: 12, marginBottom: 20 }}>
            {REVIEWS.map((r, i) => (
              <div key={i} style={cardStyle}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 6 }}>
                  <span style={{ fontWeight: 600, fontSize: 13, color: colors.text }}>{r.name}</span>
                  <Stars rating={r.rating} size={12} />
                </div>
                <p style={{ fontSize: 13, color: colors.textMuted, margin: 0, lineHeight: 1.5 }}>{lang === "hi" ? r.hi : r.en}</p>
              </div>
            ))}
          </div>

          {!reviewSubmitted ? (
            <div style={cardStyle}>
              <h4 style={{ fontSize: 14, fontWeight: 700, color: colors.text, margin: "0 0 12px" }}>{t.writeReview}</h4>
              <Field label={t.yourRating} colors={colors}>
                <div style={{ display: "flex", gap: 4 }}>
                  {[1, 2, 3, 4, 5].map((i) => (
                    <button
                      key={i}
                      onClick={() => setReviewRating(i)}
                      style={{ background: "none", border: "none", cursor: "pointer", padding: 2 }}
                      aria-label={`${i} stars`}
                    >
                      <Icon name="star" size={20} color={i <= reviewRating ? colors.urgent : colors.border} />
                    </button>
                  ))}
                </div>
              </Field>
              <Field label={t.yourReview} colors={colors}>
                <textarea
                  value={reviewText}
                  onChange={(e) => setReviewText(e.target.value)}
                  rows={3}
                  style={{ ...selectStyle(colors), width: "100%", resize: "vertical", fontFamily: "inherit" }}
                />
              </Field>
              <button
                style={{ ...buttonPrimary, marginTop: 10 }}
                onClick={() => reviewText.trim() && setReviewSubmitted(true)}
              >
                {t.submitReview}
              </button>
            </div>
          ) : (
            <div style={{ ...cardStyle, color: colors.accent, fontSize: 13, fontWeight: 600 }}>
              {lang === "hi" ? "रिव्यू सबमिट हो गया, संचालन के बाद दिखेगा।" : "Review submitted — it will appear after moderation."}
            </div>
          )}
        </Section>
      </div>
    );
  };

  const InfoCard = ({ icon, label, value, badge, badgeColor, colors }) => (
    <div style={{ background: colors.surface, border: `1px solid ${colors.border}`, borderRadius: 14, padding: 16 }}>
      <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 6 }}>
        <Icon name={icon} size={15} color={colors.primary} />
        <span style={{ fontSize: 12, color: colors.textMuted, fontWeight: 600 }}>{label}</span>
      </div>
      <div style={{ fontSize: 14, color: colors.text, fontWeight: 500 }}>{value}</div>
      {badge && (
        <span style={{ display: "inline-block", marginTop: 8, fontSize: 11, fontWeight: 700, color: badgeColor }}>{badge}</span>
      )}
    </div>
  );

  const Field = ({ label, children, colors }) => (
    <div style={{ marginBottom: 4 }}>
      <label style={{ display: "block", fontSize: 12, fontWeight: 600, color: colors.textMuted, marginBottom: 6 }}>{label}</label>
      {children}
    </div>
  );

  /* ---------------- EMERGENCY PAGE ---------------- */
  const EMERGENCY_ITEMS = [
    { icon: "cross", en: "Hospitals", hi: "हॉस्पिटल", phone: "108" },
    { icon: "phoneCall", en: "Ambulance", hi: "एम्बुलेंस", phone: "102" },
    { icon: "bolt", en: "Electricians", hi: "इलेक्ट्रीशियन", phone: "+91 98765 43210" },
    { icon: "droplet", en: "Plumbers", hi: "प्लंबर", phone: "+91 98765 11223" },
    { icon: "check", en: "Police stations", hi: "पुलिस स्टेशन", phone: "100" },
    { icon: "droplet", en: "Blood banks", hi: "ब्लड बैंक", phone: "104" },
  ];

  const EmergencyPage = () => (
    <div style={{ maxWidth: 900, margin: "0 auto", padding: "32px 24px 64px" }}>
      <h1 style={{ fontSize: 24, fontWeight: 800, color: colors.text, margin: "0 0 6px" }}>{t.emergencyTitle}</h1>
      <p style={{ fontSize: 13, color: colors.textMuted, margin: "0 0 24px" }}>{t.emergencySub}</p>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 14 }}>
        {EMERGENCY_ITEMS.map((item, i) => (
          <a
            key={i}
            href={`tel:${item.phone}`}
            style={{
              ...cardStyle,
              textDecoration: "none",
              display: "flex",
              alignItems: "center",
              gap: 14,
              borderColor: `${colors.urgent}40`,
            }}
          >
            <div
              style={{
                width: 44,
                height: 44,
                borderRadius: 12,
                background: `${colors.urgent}1A`,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                flexShrink: 0,
              }}
            >
              <Icon name={item.icon} size={20} color={colors.urgent} />
            </div>
            <div>
              <div style={{ fontWeight: 700, fontSize: 14, color: colors.text }}>{lang === "hi" ? item.hi : item.en}</div>
              <div style={{ fontSize: 12, color: colors.textMuted }}>{item.phone}</div>
            </div>
          </a>
        ))}
      </div>
    </div>
  );

  return (
    <div style={{ background: colors.bg, minHeight: "100vh", fontFamily: "'Inter', 'Manrope', system-ui, sans-serif", color: colors.text }}>
      <Navbar />
      {page === "home" && <HomePage />}
      {page === "directory" && <DirectoryPage />}
      {page === "profile" && <ProfilePage />}
      {page === "emergency" && <EmergencyPage />}
      <div style={{ borderTop: `1px solid ${colors.border}`, padding: "24px", textAlign: "center", fontSize: 12, color: colors.textMuted }}>
        {t.brand} &middot; {lang === "hi" ? "प्रोटोटाइप — डिज़ाइन प्रिव्यू" : "Prototype — design preview"}
      </div>
    </div>
  );
}

function selectStyle(colors) {
  return {
    border: `1px solid ${colors.border}`,
    borderRadius: 10,
    padding: "9px 12px",
    fontSize: 13,
    background: colors.surface,
    color: colors.text,
    outline: "none",
  };
}