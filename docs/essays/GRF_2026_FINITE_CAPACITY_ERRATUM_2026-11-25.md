# GRF finite-capacity essay mathematical erratum

Base: `c61bb8726ebce47e7797555b66fdad518cd0c253`.

Source: [original essay](GRF_2026_FINITE_CAPACITY_SPACETIME_DEFLECTION.tex); original blob `b09bbc61287c2710d8a1bccbc94824785cf5cec1`.

For the Euclidean spatial gradient and Hessian operator norm, put $f=\log n$. On $r>0$, $\nabla^2f=f''\hat r\hat r^T+(f'/r)(I-\hat r\hat r^T)$. Thus the capacity bound on an annulus is $M_1/n_{\min}+\max\{M_2/n_{\min}+M_1^2/n_{\min}^2,M_1/(r_0n_{\min})\}$. The old bound omits the tangential eigenvalue: for $n=1+r$ on $[1/100,1/50]$, at $r=1/100$ the tangential eigenvalue is $10000/101$, whereas the old bound with $M_1=1,M_2=0,n_{\min}=101/100$ is less than $2$. The exponential radial example is valid on compact annuli but is not differentiable at the spatial origin. Replace it for a smooth central model by $n=1-\varepsilon e^{-r^2/R^2}$, with $0<\varepsilon<1$, $R>0$. Its full spatial gradient and Hessian are bounded, as are those of $\log n$. For a Euclidean unit ray tangent $T$, Fermat's equation gives $dT/ds=(I-TT^T)\nabla\log n$; the radial component of this bending is $(n'/n)(1-(T\cdot\hat r)^2)$, nonnegative and strictly positive for nonradial rays where $n'>0$. This is a local bending statement, not a universal scattering-angle or stability theorem. Interpreted as a physical Einstein metric with flat spatial slices and lapse $N=\sqrt{\alpha}$, the orthonormal density and radial pressure satisfy $8\pi\rho=0$ and $8\pi p_r=2N'/(rN)=\alpha'/(r\alpha)$ in units $G=c=1$ with no cosmological constant. Hence $\alpha'<0$ violates the radial null energy condition. Optical realizability does not establish gravitational stress-energy admissibility. Bounded derivatives do not by themselves prove finite material bandwidth or perturbative stability. The finite-capacity criterion remains a proposed screen, not a sufficient physical realizability theorem. This correction concerns the one-function essay ansatz, not the separate two-function or encoded certificate-chain results.

## Derivations

For the Gaussian profile write \(x\in\mathbb R^3\), \(u=|x|^2/R^2\), and \(n(x)=1-\varepsilon e^{-u}\). Then
\[
\nabla n=2\varepsilon R^{-2}e^{-u}x,\qquad
\nabla^2 n=2\varepsilon R^{-2}e^{-u}(I-2xx^T/R^2).
\]
The tangential and radial Hessian eigenvalues are \(2\varepsilon R^{-2}e^{-u}\) and \(2\varepsilon R^{-2}(1-2u)e^{-u}\). For \(u\ge0\), \(|1-2u|e^{-u}\le1\); consequently
\[
\|\nabla n\|\le \sqrt{2/e}\,\varepsilon/R,\quad
\|\nabla^2 n\|_{\rm op}\le 2\varepsilon/R^2.
\]
Since \(n\ge1-\varepsilon\), the log gradient is bounded by the first bound divided by \(1-\varepsilon\), and the log Hessian by the second bound divided by \(1-\varepsilon\) plus the squared log-gradient bound. These estimates also hold at the origin. The profile is an idealized optical index, not a verified manufactured material.

For \(g=-N^2dt^2+\delta_{ij}dx^idx^j\), the static curvature formulas are \(R_{tt}=N\Delta N\), \(R_{ij}=-N^{-1}\partial_i\partial_jN\), and scalar curvature \(\mathcal R=-2N^{-1}\Delta N\). Hence \(G_{\hat t\hat t}=0\) and \(G_{\hat r\hat r}=N^{-1}(\Delta N-N'')=2N'/(rN)\). With \(G_{\mu\nu}=8\pi T_{\mu\nu}\), radial null contraction is negative wherever \(N'<0\). No conclusion about the separate two-function realization follows from this obstruction.

The repository's existing finite-capacity source audits already acknowledge the analogue/Einstein-matter distinction and the one-function obstruction. This erratum makes those restrictions explicit in the essay and repairs the spatial derivative estimates. Existing certificate-chain claims are not independently audited here.

Paper derivations only. No new Lean verification, physical experiment, or PDF regeneration.
