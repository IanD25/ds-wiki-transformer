# Prior-Art Gate — Thermo / RG / NE Cluster

**Date:** 2026-04-19
**Scope:** 25 entries — TD1-2, TD4-14 + RG01-06 + NE01-06
**Template seed:** TD3 (anchored 2026-04-18) provides Callen + Reif + Clausius 1865 + Carathéodory 1909 + Lieb-Yngvason 1999 basis.

---

## Sub-cluster split

| Sub | Entries | Topic | Shared anchors |
|---|---|---|---|
| A | TD1-2, TD4-14 (13) | Classical thermodynamics laws + applied laws | Callen + Reif (verified at TD3); add Pathria for some |
| B | RG01-06 (6) | Renormalization group | Cardy + Goldenfeld (medium ISBN); per-paper progenitor DOIs |
| C | NE01-06 (6) | Non-equilibrium thermodynamics + fluctuation theorems | Kondepudi-Prigogine (medium ISBN); per-paper progenitor DOIs; Seifert 2012 RPP review |

---

## Sub-A — Classical thermodynamics (13 entries)

| Entry | Title | Progenitor | Notes |
|---|---|---|---|
| TD1 | Zeroth Law of Thermodynamics | R.H. Fowler 1931 (no DOI) → anchor via Callen Ch. 1 | Anchored as `axiomatic_foundation` only via textbook; Fowler text not online. |
| TD2 | First Law of Thermodynamics | Joule 1850 *Phil. Trans.* (DOI 10.1098/rstl.1850.0004) | + Mayer 1842, Helmholtz 1847 (no individual DOIs) |
| TD4 | Third Law of Thermodynamics | Nernst 1906 *Nachr. Ges. Wiss. Göttingen* (no DOI) → Planck 1911 reformulation | Anchored via Callen Ch. 10 |
| TD5 | Fundamental Thermodynamic Relation | Gibbs 1875-1878 "On the Equilibrium of Heterogeneous Substances" (collected works) | Anchored via Callen Ch. 2-3 |
| TD6 | Onsager Reciprocal Relations | Onsager 1931 PR 37, 405 (DOI 10.1103/PhysRev.37.405) + PR 38, 2265 (DOI 10.1103/PhysRev.38.2265) | APS DOI pattern |
| TD7 | Boltzmann Equation | Boltzmann 1872 *Wien. Sitzungsber.* 66, 275 (no DOI) | Anchored via Cercignani 1988 textbook |
| TD8 | Carnot's Theorem | Carnot 1824 *Réflexions sur la puissance motrice du feu* (book) | ISBN 978-0486446417 (Dover reprint, medium) |
| TD9 | Newton's Law of Cooling | Newton 1701 *Phil. Trans.* (no DOI but well-documented) | Anchored via textbooks |
| TD10 | Fourier's Law of Heat Conduction | Fourier 1822 *Théorie analytique de la chaleur* (book; English: Cambridge 1878) | ISBN 978-0521539685 (Cambridge classic) |
| TD11 | Kopp's Law | Kopp 1864 *Annalen der Chemie und Pharmacie* 126, 362 (no modern DOI) | Anchored via standard chemistry textbook (Atkins) |
| TD12 | Dulong-Petit Law | Dulong-Petit 1819 *Annales de Chimie et Physique* 10, 395 (no DOI) | Anchored via Reif Ch. 7 |
| TD13 | Carnot Efficiency | Same as TD8 (Carnot 1824) | |
| TD14 | van der Waals Equation | van der Waals 1873 PhD thesis (DOI 10.1107/S0567739474001793 to reprint?) | Use English translation; Nobel Lecture 1910 (DOI 10.1063/1.3066856 republished?) |

**Confidence policy for old papers:**
- DOIs that follow recognized publisher patterns (APS, Wiley Annalen, Royal Society) → `high`
- Books / pre-DOI works without modern reprints with DOI → anchored via textbook citation only
- ISBNs claimed from memory → `medium` with "verify via WorldCat" note

---

## Sub-B — Renormalization Group (6 entries)

| Entry | Title | Progenitor |
|---|---|---|
| RG01 | Wilson's Renormalisation Group | Wilson 1971 PRB 4, 3174 (DOI 10.1103/PhysRevB.4.3174) + PRB 4, 3184 (DOI 10.1103/PhysRevB.4.3184) |
| RG02 | Beta Function | Gell-Mann-Low 1954 PR 95, 1300 (DOI 10.1103/PhysRev.95.1300); Callan 1970 PRD 2, 1541 (DOI 10.1103/PhysRevD.2.1541) |
| RG03 | Kadanoff Block Spin Transformation | Kadanoff 1966 *Physics* 2, 263 (no DOI; pre-Elsevier) |
| RG04 | Zamolodchikov c-Theorem | Zamolodchikov 1986 *JETP Lett.* 43, 730 (no English DOI) — anchored via Cardy Ch. 11 |
| RG05 | a-Theorem (4D) | Komargodski-Schwimmer 2011 JHEP 12, 099 (DOI 10.1007/JHEP12(2011)099) |
| RG06 | Cotler-Rezchikov: RG as Optimal Transport with Fisher Metric | Cotler-Rezchikov 2022 (arXiv:2202.11737) — recent preprint, anchor as `cites` |

Standard textbook: Cardy 1996 "Scaling and Renormalization in Statistical Physics" (ISBN 978-0521499590, medium). Add Goldenfeld 1992 "Lectures on Phase Transitions and the RG" (ISBN 978-0201554090, medium).

---

## Sub-C — Non-equilibrium (6 entries)

| Entry | Title | Progenitor |
|---|---|---|
| NE01 | Prigogine Dissipative Structures | Prigogine 1977 Nobel Lecture (DOI 10.1126/science.201.4358.777); + Glansdorff-Prigogine 1971 book |
| NE02 | Maximum Entropy Production Principle | Ziegler 1963 *Progress in Solid Mechanics* (book) + Martyushev-Seleznev 2006 *Phys. Rep.* (DOI 10.1016/j.physrep.2005.12.001) |
| NE03 | Jarzynski Equality | Jarzynski 1997 PRL 78, 2690 (DOI 10.1103/PhysRevLett.78.2690) |
| NE04 | Crooks Fluctuation Theorem | Crooks 1999 PRE 60, 2721 (DOI 10.1103/PhysRevE.60.2721) |
| NE05 | Fluctuation-Dissipation Theorem | Callen-Welton 1951 PR 83, 34 (DOI 10.1103/PhysRev.83.34) |
| NE06 | England Dissipation-Driven Adaptation | England 2013 *J. Chem. Phys.* 139, 121923 (DOI 10.1063/1.4818538); England 2015 *Nat. Nanotechnol.* 10, 919 (DOI 10.1038/nnano.2015.250) |

Standard textbook: Kondepudi-Prigogine 2014 "Modern Thermodynamics" 2nd ed (ISBN 978-1118371817, medium).
Comprehensive survey: Seifert 2012 "Stochastic thermodynamics, fluctuation theorems and molecular machines" *Rep. Prog. Phys.* 75, 126001 (DOI 10.1088/0034-4885/75/12/126001).

---

## Summary

**Totals:** ~95-100 anchors across 25 entries. Heavy use of `progenitor` role; minimal Wikipedia (most have articles, all anchored medium).

**Pending follow-ups:**
- Multiple ISBNs new to DB (Pathria, Cardy, Goldenfeld, Kondepudi, Cercignani, etc.) — flagged `medium` with "verify via WorldCat"
- Several pre-DOI papers (Carnot 1824, Fourier 1822, Kadanoff 1966, Boltzmann 1872) anchored via textbook citation rather than direct identifier
- Wikipedia oldid backfill carries forward
- TD8 + TD13 share the same Carnot 1824 source (different roles per entry)
