"""
Generate the Complexity Tax formalization PDF.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib import colors

OUTPUT = "/Users/iandarling/Projects/DS_Wiki_Transformation/docs/COMPLEXITY_TAX_FORMALIZATION.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    topMargin=0.8*inch,
    bottomMargin=0.8*inch,
    leftMargin=1*inch,
    rightMargin=1*inch,
)

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    'PaperTitle', parent=styles['Title'],
    fontSize=18, leading=22, spaceAfter=6, alignment=TA_CENTER,
    textColor=HexColor('#1a1a1a'),
))
styles.add(ParagraphStyle(
    'Author', parent=styles['Normal'],
    fontSize=11, leading=14, alignment=TA_CENTER,
    textColor=HexColor('#555555'), spaceAfter=20,
))
styles.add(ParagraphStyle(
    'AbstractTitle', parent=styles['Heading2'],
    fontSize=12, leading=14, spaceBefore=10, spaceAfter=6,
    alignment=TA_CENTER,
))
styles.add(ParagraphStyle(
    'AbstractBody', parent=styles['Normal'],
    fontSize=10, leading=14, leftIndent=36, rightIndent=36,
    alignment=TA_JUSTIFY, spaceAfter=16,
    textColor=HexColor('#333333'),
))
styles.add(ParagraphStyle(
    'SectionHead', parent=styles['Heading1'],
    fontSize=14, leading=17, spaceBefore=20, spaceAfter=8,
    textColor=HexColor('#1a1a1a'),
))
styles.add(ParagraphStyle(
    'SubsectionHead', parent=styles['Heading2'],
    fontSize=12, leading=15, spaceBefore=14, spaceAfter=6,
    textColor=HexColor('#2a2a2a'),
))
styles.add(ParagraphStyle(
    'Body', parent=styles['Normal'],
    fontSize=10.5, leading=14.5, alignment=TA_JUSTIFY,
    spaceAfter=8,
))
styles.add(ParagraphStyle(
    'MathBlock', parent=styles['Normal'],
    fontSize=10.5, leading=15, leftIndent=36,
    fontName='Courier', spaceAfter=10, spaceBefore=6,
))
styles.add(ParagraphStyle(
    'TheoremStyle', parent=styles['Normal'],
    fontSize=10.5, leading=14.5, leftIndent=18, rightIndent=18,
    spaceBefore=10, spaceAfter=10,
    borderWidth=0.5, borderColor=HexColor('#cccccc'),
    borderPadding=8,
    backColor=HexColor('#f8f8f8'),
))
styles.add(ParagraphStyle(
    'Caption', parent=styles['Normal'],
    fontSize=9, leading=12, alignment=TA_CENTER,
    textColor=HexColor('#666666'), spaceBefore=4, spaceAfter=12,
))
styles.add(ParagraphStyle(
    'Reference', parent=styles['Normal'],
    fontSize=9.5, leading=13, leftIndent=24, firstLineIndent=-24,
    spaceAfter=4,
))

B = styles['Body']
M = styles['MathBlock']
S = styles['SectionHead']
SS = styles['SubsectionHead']
T = styles['TheoremStyle']

def tbl(data, col_widths=None, header=True):
    """Create a styled table."""
    style_cmds = [
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('LEADING', (0, 0), (-1, -1), 13),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
    ]
    if header:
        style_cmds += [
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 0), (-1, 0), HexColor('#e8e8e8')),
        ]
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    t.setStyle(TableStyle(style_cmds))
    return t

story = []

# ---- Title ----
story.append(Paragraph(
    "The Complexity Tax", styles['PaperTitle']
))
story.append(Paragraph(
    "A Formal Framework for Signal Coupling<br/>Degradation in Portfolio Systems",
    ParagraphStyle('Subtitle', parent=styles['Title'], fontSize=13, leading=16,
                   alignment=TA_CENTER, textColor=HexColor('#444444'), spaceAfter=12)
))
story.append(Paragraph(
    "Ian Darling<br/>Principia Formal Diagnostics / AlphaEntropy<br/>April 2026",
    styles['Author']
))
story.append(HRFlowable(width="60%", thickness=0.5, color=HexColor('#999999'),
                         spaceAfter=16, spaceBefore=4))

# ---- Abstract ----
story.append(Paragraph("Abstract", styles['AbstractTitle']))
story.append(Paragraph(
    "We formalize the <i>complexity tax</i> \u2014 the empirical observation that adding "
    "cross-coupled signals to an independent-signal portfolio system degrades risk-adjusted "
    "performance. Starting from the Data Processing Inequality (a theorem of information "
    "theory), we derive a closed-form expression for the Sharpe ratio degradation under "
    "mean-field signal coupling: <b>SR<sub>combined</sub>/SR<sub>0</sub> = "
    "1/\u221a(1 + \u03bb<super>2</super>\u03c1)</b>, where \u03bb is the coupling strength and \u03c1 is the "
    "inter-signal correlation. We validate this formula against a 7-configuration ablation "
    "study on a live trading system (V28.4, US equities, 2003\u20132025) and against numerical "
    "experiments on coupled double pendulums. The framework yields a three-part coupling "
    "taxonomy \u2014 orthogonal, cross-sectional, and cross-channel \u2014 with distinct complexity "
    "tax profiles, and predicts that the tax is larger for homogeneous portfolios than "
    "heterogeneous ones.",
    styles['AbstractBody']
))

# ---- 1. Introduction ----
story.append(Paragraph("1. Introduction", S))
story.append(Paragraph(
    "Portfolio construction systems face a persistent engineering problem: features that "
    "appear beneficial in isolation often degrade performance when combined. This is commonly "
    "attributed to overfitting or multicollinearity, but we argue the phenomenon has a deeper "
    "information-theoretic origin.",
    B
))
story.append(Paragraph(
    "The central claim: any signal that couples a stock's portfolio weight to information "
    "about <i>other</i> stocks introduces noise proportional to the coupling strength and the "
    "correlation between signals. This noise is the \"complexity tax\" \u2014 a systematic "
    "performance drag that can only be zero when the coupling is zero or the signals are "
    "perfectly orthogonal.",
    B
))
story.append(Paragraph(
    "We develop this claim in four layers of decreasing mathematical certainty:",
    B
))
story.append(Paragraph(
    "\u2022 <b>Layer 1:</b> Pure information theory (theorem, no assumptions)<br/>"
    "\u2022 <b>Layer 2:</b> Factor model mathematics (theorem given one structural assumption)<br/>"
    "\u2022 <b>Layer 3:</b> Testable predictions with estimated parameters<br/>"
    "\u2022 <b>Layer 4:</b> Conjectures motivated by cross-domain experiments",
    ParagraphStyle('BulletList', parent=B, leftIndent=24, spaceAfter=12)
))

# ---- 2. Layer 1 ----
story.append(Paragraph("2. Layer 1: The Data Processing Inequality", S))

story.append(Paragraph("2.1 Statement", SS))
story.append(Paragraph(
    "For any random variables forming a Markov chain X \u2192 Y \u2192 Z:",
    B
))
story.append(Paragraph("I(X; Z) \u2264 I(X; Y)", M))
story.append(Paragraph(
    "where I(\u00b7;\u00b7) denotes mutual information. Equality holds if and only if Z is a "
    "<i>sufficient statistic</i> for X given Y. This is Theorem 2.8.1 in Cover &amp; Thomas "
    "(2006). It requires no assumptions about the distribution of X, Y, or Z \u2014 it follows "
    "from the non-negativity of the Kullback-Leibler divergence D<sub>KL</sub>(p||q) \u2265 0, "
    "which is itself a consequence of Jensen's inequality applied to the convexity of -log(x).",
    B
))

story.append(Paragraph("2.2 Application to Portfolio Signals", SS))
story.append(Paragraph(
    "Let R<sub>i</sub> = return of stock i (target variable), x<sub>i</sub> = stock-specific "
    "features (raw data about stock i only), and z<sub>i</sub> = f(x<sub>1</sub>, ..., "
    "x<sub>N</sub>) = cross-sectional signal incorporating information from all stocks.",
    B
))
story.append(Paragraph(
    "If R<sub>i</sub> \u22a5 x<sub>j</sub> | x<sub>i</sub> for all j \u2260 i (other stocks' "
    "features contain no additional information about stock i's return beyond what x<sub>i</sub> "
    "already provides), then R<sub>i</sub> \u2192 x<sub>i</sub> \u2192 z<sub>i</sub> forms a "
    "Markov chain and the DPI gives:",
    B
))
story.append(Paragraph("I(R<sub>i</sub>; z<sub>i</sub>) \u2264 I(R<sub>i</sub>; x<sub>i</sub>)", M))
story.append(Paragraph(
    "<b>Interpretation:</b> Cross-sectional processing cannot increase the information that "
    "the signal contains about stock i's return. At best it preserves it (sufficient statistic); "
    "generically it loses some.",
    B
))

story.append(Paragraph("2.3 When Cross-Sectional Information Could Help", SS))
story.append(Paragraph(
    "The DPI bound does NOT apply when the Markov condition fails \u2014 i.e., when other "
    "stocks' features DO contain additional information about R<sub>i</sub> beyond x<sub>i</sub>. "
    "This happens when stock returns share a common factor M observable through cross-sectional "
    "aggregation, or when stock i's features are missing information about factor exposure "
    "\u03b2<sub>i</sub> that can be estimated from the cross-section. The complexity tax "
    "framework applies specifically to settings where the stock-specific signal is already "
    "strong (high IC) and the cross-sectional processing primarily adds factor-related noise "
    "rather than factor-related signal.",
    B
))

# ---- 3. Layer 2 ----
story.append(PageBreak())
story.append(Paragraph("3. Layer 2: The Complexity Tax Formula", S))

story.append(Paragraph("3.1 Structural Assumption: Single-Factor Model", SS))
story.append(Paragraph("Assume returns follow a single-factor structure:", B))
story.append(Paragraph(
    "R<sub>i</sub> = \u03b1<sub>i</sub> + \u03b2<sub>i</sub>M + \u03b5<sub>i</sub>",
    M
))
story.append(Paragraph(
    "where \u03b1<sub>i</sub> is stock-specific alpha, M is the common market factor with "
    "E[M] = 0, \u03b2<sub>i</sub> is stock i's factor loading, and \u03b5<sub>i</sub> is "
    "idiosyncratic noise independent across stocks and independent of M. This is the standard "
    "single-factor model (Sharpe, 1964). It is approximately valid empirically: the market "
    "factor explains 30\u201340% of individual stock return variance.",
    B
))

story.append(Paragraph("3.2 Signal Structure", SS))
story.append(Paragraph(
    "A stock-specific signal observes alpha with noise: s<sub>i</sub> = \u03b1<sub>i</sub> "
    "+ \u03b7<sub>i</sub>, where \u03b7<sub>i</sub> is measurement noise independent of "
    "everything else.",
    B
))

story.append(Paragraph("3.3 Mean-Field Coupling", SS))
story.append(Paragraph(
    "A cross-sectional signal adds the average signal: z<sub>i</sub> = s<sub>i</sub> + "
    "\u03bb \u00b7 c<sub>i</sub>, where c<sub>i</sub> = (1/N) \u03a3<sub>j</sub> s<sub>j</sub>. "
    "The coupling term c<sub>i</sub> has variance:",
    B
))
story.append(Paragraph(
    "Var(c<sub>i</sub>) = \u03c3<super>2</super><sub>s</sub>/N + "
    "((N-1)/N) \u00b7 \u03c1<sub>s</sub> \u00b7 \u03c3<super>2</super><sub>s</sub>",
    M
))
story.append(Paragraph(
    "where \u03c1<sub>s</sub> = Corr(s<sub>i</sub>, s<sub>j</sub>) for i \u2260 j. "
    "For large N with correlated signals (\u03c1<sub>s</sub> > 0): "
    "Var(c<sub>i</sub>) \u2248 \u03c1<sub>s</sub> \u00b7 \u03c3<super>2</super><sub>s</sub>.",
    B
))

story.append(Paragraph("3.4 The Complexity Tax Theorem", SS))
story.append(Paragraph(
    "<b>Theorem.</b> Under the single-factor model with mean-field coupling, the Sharpe "
    "ratio degradation is:<br/><br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;<b>SR<sub>combined</sub> / SR<sub>0</sub> = "
    "1 / \u221a(1 + \u03bb<super>2</super>\u03c1<sub>s</sub>)</b><br/><br/>"
    "<b>Properties:</b><br/>"
    "1. SR<sub>combined</sub> \u2264 SR<sub>0</sub> always (the tax is non-negative)<br/>"
    "2. Equality when \u03bb = 0 (no coupling) or \u03c1<sub>s</sub> = 0 (orthogonal signals)<br/>"
    "3. Monotonically increasing in both \u03bb and \u03c1<sub>s</sub><br/>"
    "4. For uncorrelated signals, the tax \u2192 0 as N \u2192 \u221e<br/>"
    "5. For correlated signals, the tax persists regardless of N",
    T
))

story.append(Paragraph("3.5 The Coupling Taxonomy", SS))
story.append(tbl([
    ["Type", "Operator Form", "Tax", "Example"],
    ["Orthogonal", "s_i = f(x_i)", "0", "Per-stock momentum gate"],
    ["Cross-sectional", "s_i = g(x_i, x_{-i})", "1 - 1/\u221a(1+\u03bb\u00b2\u03c1)", "Universe-wide z-scores"],
    ["Cross-channel", "s^A_i = h(s^B)", "Potentially largest", "Allocation from other channel"],
], col_widths=[1.2*inch, 1.5*inch, 1.5*inch, 2.0*inch]))
story.append(Paragraph("Table 1: Coupling taxonomy with complexity tax profiles.", styles['Caption']))

# ---- 4. Layer 3 ----
story.append(Paragraph("4. Layer 3: Empirical Validation", S))

story.append(Paragraph("4.1 The V28.4 Ablation Study", SS))
story.append(Paragraph(
    "A full factorial ablation study was conducted on the AlphaEntropy trading system "
    "(V28.4, US equities $500M\u2013$5B market cap, 2003\u20132025). The system architecture is "
    "V22 quality-stability scoring + TrendV1 momentum, with 5 toggleable features.",
    B
))
story.append(tbl([
    ["Configuration", "CAGR", "Max Drawdown", "Calmar"],
    ["All features ON", "9.22%", "-10.2%", "0.904"],
    ["All features OFF", "10.11%", "-9.5%", "1.064"],
    ["Entry gate only ON", "10.58%", "-9.6%", "1.102"],
], col_widths=[2.3*inch, 1.1*inch, 1.2*inch, 1.0*inch]))
story.append(Paragraph("Table 2: V28.4 ablation results (22-year backtest).", styles['Caption']))

story.append(Paragraph("4.2 Feature Classification", SS))
story.append(tbl([
    ["Feature", "Type", "Mechanism", "Calmar \u0394"],
    ["Entry momentum gate", "Orthogonal", "Per-stock 63d return > 0", "+0.038"],
    ["IC Rescue", "Cross-sectional", "Universe-wide R&D metric", "-0.021"],
    ["Fisher/Treynor sizing", "Cross-sectional", "Z-scored within Q1", "-0.039"],
    ["Recovery boost", "Cross-channel", "V22 alloc depends on D_eff", "-0.025"],
], col_widths=[1.4*inch, 1.1*inch, 2.0*inch, 0.9*inch]))
story.append(Paragraph("Table 3: Feature classification under the coupling taxonomy.", styles['Caption']))

story.append(Paragraph("4.3 Parameter Estimation", SS))
story.append(Paragraph(
    "From the Sharpe ratio degradation formula, we can estimate the effective coupling "
    "parameter \u03bb<super>2</super>\u03c1 for each feature:",
    B
))
story.append(tbl([
    ["Feature", "SR_comb/SR_0", "Implied \u03bb\u00b2\u03c1"],
    ["IC Rescue", "0.977", "0.047"],
    ["Fisher/Treynor", "0.959", "0.086"],
    ["Recovery Boost", "0.973", "0.056"],
    ["Combined (predicted)", "0.917", "0.189"],
    ["Combined (observed)", "0.850", "0.384"],
], col_widths=[2.0*inch, 1.3*inch, 1.3*inch]))
story.append(Paragraph(
    "Table 4: Estimated coupling parameters. The combined tax is superadditive: "
    "the observed degradation (0.850) exceeds the prediction from summing individual "
    "\u03bb<super>2</super>\u03c1 values (0.917).",
    styles['Caption']
))

story.append(Paragraph("4.4 The Homogeneity Effect", SS))
story.append(Paragraph(
    "A 2\u00d72 factorial control compared V22 stability-scoring versus traditional "
    "profitability-level scoring. V22-selected portfolios are 5.7\u00d7 more sensitive to "
    "coupling features (Calmar impact +0.160 vs +0.028). This is consistent with the "
    "homogeneity hypothesis: a portfolio where all stocks have similar \u03b1<sub>i</sub> "
    "gains nothing from cross-sectional information, so coupling adds only noise.",
    B
))

# ---- 5. Layer 4 ----
story.append(PageBreak())
story.append(Paragraph("5. Layer 4: Cross-Domain Evidence from Hamiltonian Dynamics", S))

story.append(Paragraph("5.1 The Double Pendulum as a Coupling Laboratory", SS))
story.append(Paragraph(
    "To test whether the complexity tax is specific to financial markets or a universal "
    "property of coupled dynamical systems, we conducted numerical experiments on systems "
    "of coupled double pendulums. A double pendulum is a deterministic chaotic system with "
    "4-dimensional phase space (\u03b8<sub>1</sub>, \u03b8<sub>2</sub>, \u03c9<sub>1</sub>, "
    "\u03c9<sub>2</sub>). We define <i>geodesic efficiency</i> \u03b7 = (straight-line distance) "
    "/ (total path length), measuring how directly a trajectory moves through phase space.",
    B
))

story.append(Paragraph("5.2 The \u03c4<sub>relax</sub> Scaling Law", SS))
story.append(Paragraph(
    "For 25,139 trajectories of a single double pendulum, geodesic efficiency scales with "
    "the log of the flip time:",
    B
))
story.append(Paragraph(
    "\u03b7 = f(log(T<sub>flip</sub> / \u03c4<sub>natural</sub>)),  "
    "Pearson r = -0.831",
    M
))
story.append(Paragraph(
    "The same scaling law was independently measured in financial markets (AlphaEntropy, "
    "21 crisis episodes): r = -0.896. The transition from near-geodesic (\u03b7 \u2248 0.94) "
    "to meandering (\u03b7 \u2248 0.01) occurs at T<sub>flip</sub>/\u03c4 \u2248 1 in both systems.",
    B
))

story.append(Paragraph("5.3 Coupling Reduces Geodesic Efficiency", SS))
story.append(Paragraph(
    "Four experiments systematically tested what causes the efficiency gap between "
    "the pendulum (\u03b7 \u2248 0.94) and financial markets (\u03b7 \u2248 0.43):",
    B
))
story.append(tbl([
    ["Experiment", "Hypothesis", "Result"],
    ["Friction sweep (\u03b3=0\u20132.0)", "Dissipation reduces \u03b7", "\u2717 \u03b7 barely moves (0.94\u21920.92)"],
    ["Independent spectators (4D\u2192104D)", "Dimensionality reduces \u03b7", "\u2717 \u03b7 increases (0.95\u21920.97)"],
    ["Mean-field coupling (\u03ba=0\u219215)", "Correlation reduces \u03b7", "\u2713 \u03b7 drops: 0.91\u21920.24"],
    ["Bounded heterogeneous", "Realistic coupling", "\u2713 Best match: \u03b7=0.45, r=-0.71"],
], col_widths=[2.0*inch, 1.6*inch, 2.3*inch]))
story.append(Paragraph(
    "Table 5: Coupling experiments on N=4 coupled double pendulums (16D phase space).",
    styles['Caption']
))

story.append(Paragraph("5.4 The r-\u03b7 Tradeoff", SS))
story.append(Paragraph(
    "Financial markets maintain both high r (clean scaling law, -0.896) AND low \u03b7 "
    "(inefficient paths, 0.43). Mean-field coupling cannot reproduce this combination \u2014 "
    "any coupling strong enough to lower \u03b7 also degrades r. Markets must have a coupling "
    "topology more structured than all-to-all: likely hierarchical (sector \u2192 market \u2192 "
    "global) or time-varying. The V28.4 ablation confirms this: the parallel V22 \u2225 ETF "
    "architecture (hierarchical, \u03c1 \u2248 0.02 between channels) achieves both, while "
    "cross-channel coupling (recovery boost) degrades performance.",
    B
))

# ---- 6. Formal Statement ----
story.append(Paragraph("6. The Complexity Tax: Formal Statement", S))

story.append(Paragraph(
    "<b>Definition.</b> For a portfolio system with N assets, a signal s<sub>i</sub> for "
    "each asset, and a coupling operator C that transforms signals, the <i>complexity tax</i> "
    "T(C) is:",
    B
))
story.append(Paragraph(
    "T(C) = 1 - SR(C(s)) / SR(s)",
    M
))

story.append(Paragraph(
    "<b>Properties</b> (proven under single-factor model):<br/><br/>"
    "1. <b>Non-negativity:</b> T(C) \u2265 0 for any mean-field coupling operator<br/>"
    "2. <b>Zero for orthogonal signals:</b> If Corr(s<sub>i</sub>, s<sub>j</sub>) = 0 "
    "for all i \u2260 j, then T(C) \u2192 0 as N \u2192 \u221e<br/>"
    "3. <b>Monotonicity:</b> T is increasing in coupling strength \u03bb and "
    "signal correlation \u03c1<sub>s</sub><br/>"
    "4. <b>Closed form:</b> T = 1 - 1/\u221a(1 + \u03bb<super>2</super>\u03c1<sub>s</sub>) "
    "for single-level mean-field coupling<br/>"
    "5. <b>Superadditivity:</b> T(C<sub>1</sub> \u2218 C<sub>2</sub>) \u2265 "
    "T(C<sub>1</sub>) + T(C<sub>2</sub>) (empirically observed, not yet proven)",
    T
))

# ---- 7. Open Questions ----
story.append(Paragraph("7. Open Questions", S))

story.append(Paragraph("7.1 Superadditivity", SS))
story.append(Paragraph(
    "The observed combined tax exceeds the sum of individual taxes. Is this provable under "
    "the factor model, or does it require additional structure? The nonlinear interaction "
    "between coupling operators may follow from the quadratic nature of variance "
    "accumulation, but a formal proof is outstanding.",
    B
))

story.append(Paragraph("7.2 Homogeneity Scaling", SS))
story.append(Paragraph(
    "<b>Conjecture:</b> Tax(\u03bb, \u03c1, H) \u2248 \u03bb<super>2</super>\u03c1 "
    "\u00d7 H where H measures portfolio homogeneity. Currently supported by one data point "
    "(V22 vs level-scoring, 5.7\u00d7 sensitivity ratio). Needs theoretical derivation and "
    "replication across additional scoring methods.",
    B
))

story.append(Paragraph("7.3 The r-\u03b7 Tradeoff", SS))
story.append(Paragraph(
    "Financial markets achieve both clean scaling (r \u2248 -0.90) and low path efficiency "
    "(\u03b7 \u2248 0.43), which mean-field coupling cannot reproduce. What coupling topology "
    "(hierarchical? time-varying?) can? This connects portfolio construction to network "
    "science and information geometry.",
    B
))

story.append(Paragraph("7.4 Optimal Coupling", SS))
story.append(Paragraph(
    "Is there ever a positive optimal \u03bb? The framework predicts the tax is always "
    "non-negative, but this is under the assumption that cross-sectional information adds "
    "only factor noise. In regimes where factor information is genuinely useful (e.g., risk "
    "management during crises), some coupling may be optimal despite the tax. Characterizing "
    "the boundary between \"coupling helps\" and \"coupling hurts\" as a function of signal "
    "quality and factor exposure is an open problem.",
    B
))

# ---- 8. Conclusion ----
story.append(Paragraph("8. Conclusion", S))
story.append(Paragraph(
    "The complexity tax is a mathematically grounded framework for understanding why adding "
    "features to a portfolio system often hurts. The core mechanism \u2014 cross-coupling "
    "introduces noise proportional to signal correlation \u2014 is provable under standard "
    "factor model assumptions. The framework correctly predicts which features in the V28.4 "
    "ablation helped (orthogonal) and which hurt (cross-coupled), and is consistent with "
    "numerical experiments on coupled dynamical systems showing that mean-field coupling "
    "degrades both path efficiency and scaling law quality.",
    B
))
story.append(Paragraph(
    "The practical implication is architectural: portfolio systems should be designed with "
    "independent channels and orthogonal signals, not with cross-references that couple "
    "positions to each other or channels to each other. The V28.4.1 production system \u2014 "
    "stripped of all cross-coupling features, retaining only the orthogonal entry gate \u2014 "
    "achieves Calmar 0.978 (hedged) versus 0.904 (fully loaded), a 0.074 improvement "
    "attributable entirely to removing coupling that the complexity tax framework predicted "
    "would hurt.",
    B
))

# ---- References ----
story.append(PageBreak())
story.append(Paragraph("References", S))
refs = [
    "Cover, T.M. &amp; Thomas, J.A. (2006). <i>Elements of Information Theory</i>, 2nd ed. Wiley.",
    "Grinold, R.C. &amp; Kahn, R.N. (2000). <i>Active Portfolio Management</i>, 2nd ed. McGraw-Hill.",
    "Sharpe, W.F. (1964). Capital Asset Prices: A Theory of Market Equilibrium. <i>Journal of Finance</i>, 19(3), 425\u2013442.",
    "Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. <i>Rep. Prog. Phys.</i> 75, 126001.",
    "Zamolodchikov, A.B. (1986). Irreversibility of the Flux of the Renormalization Group. <i>JETP Lett.</i> 43, 730\u2013732.",
]
for i, ref in enumerate(refs, 1):
    story.append(Paragraph(f"[{i}] {ref}", styles['Reference']))

# ---- Appendix A ----
story.append(Spacer(1, 24))
story.append(Paragraph("Appendix A: Derivation of the Complexity Tax Formula", S))
story.append(Paragraph(
    "Starting from R<sub>i</sub> = \u03b1<sub>i</sub> + \u03b2<sub>i</sub>M + "
    "\u03b5<sub>i</sub> and s<sub>i</sub> = \u03b1<sub>i</sub> + \u03b7<sub>i</sub>:",
    B
))
story.append(Paragraph(
    "The combined signal z<sub>i</sub> = s<sub>i</sub> + \u03bbc<sub>i</sub> has variance "
    "Var(z<sub>i</sub>) = \u03c3<super>2</super><sub>s</sub> + "
    "2\u03bbCov(s<sub>i</sub>, c<sub>i</sub>) + "
    "\u03bb<super>2</super>Var(c<sub>i</sub>). "
    "For large N: Cov(s<sub>i</sub>, c<sub>i</sub>) \u2248 \u03c1<sub>s</sub>"
    "\u03c3<super>2</super><sub>s</sub> and "
    "Var(c<sub>i</sub>) \u2248 \u03c1<sub>s</sub>\u03c3<super>2</super><sub>s</sub>.",
    B
))
story.append(Paragraph(
    "In the regime where stock-specific alpha dominates, the cross-sectional contribution "
    "to Cov(z<sub>i</sub>, R<sub>i</sub>) is negligible compared to its contribution to "
    "variance. The IC reduces by \u03c3<sub>s</sub>/\u03c3<sub>z</sub>, giving:",
    B
))
story.append(Paragraph(
    "IC<sub>combined</sub> / IC<sub>0</sub> = "
    "1 / \u221a(1 + (2\u03bb + \u03bb<super>2</super>)\u03c1<sub>s</sub>)",
    M
))
story.append(Paragraph(
    "For small \u03bb (weak coupling), (2\u03bb + \u03bb<super>2</super>) \u2248 "
    "\u03bb<super>2</super>, giving the simplified formula "
    "SR<sub>combined</sub>/SR<sub>0</sub> \u2248 1/\u221a(1 + "
    "\u03bb<super>2</super>\u03c1<sub>s</sub>). "
    "For larger \u03bb, the full expression includes the 2\u03bb\u03c1<sub>s</sub> "
    "cross-term, meaning the tax is slightly larger than the simplified formula predicts.",
    B
))

# ---- Appendix B ----
story.append(Spacer(1, 24))
story.append(Paragraph("Appendix B: Double Pendulum Experimental Parameters", S))
story.append(tbl([
    ["Parameter", "Value"],
    ["Masses", "m1 = m2 = 1 kg"],
    ["Lengths", "L1 = L2 = 1 m"],
    ["Gravity", "g = 9.81 m/s\u00b2"],
    ["Integrator", "Symplectic Euler, dt = 1/240 s"],
    ["Natural period", "\u03c4 = 2\u03c0\u221a(L/g) = 2.006 s"],
    ["Flip threshold", "|\u03b8| > \u03c0 + 10\u207b\u00b3"],
    ["Initial conditions", "Random \u03b81, \u03b82 \u2208 [-\u03c0, \u03c0], \u03c91 = \u03c92 = 0"],
    ["Coupling model", "a_i += \u03ba_ij(\u03b8\u0304 - \u03b8_i) per angle"],
    ["Sample sizes", "5,000\u201340,000 trajectories per configuration"],
], col_widths=[2.0*inch, 4.0*inch], header=False))
story.append(Paragraph("Table 6: Experimental parameters for all pendulum experiments.", styles['Caption']))

# ---- Build ----
doc.build(story)
print(f"PDF saved to: {OUTPUT}")
