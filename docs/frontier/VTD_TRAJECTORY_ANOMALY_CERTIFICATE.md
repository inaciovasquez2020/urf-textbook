# VTD — Conditional Trajectory-Anomaly Certificate

## Definition

Let

\[
D=\{(t_i,z_i)\}_{i=1}^{N},\qquad t_1<\cdots<t_N,
\]

be a vacuum vertical trajectory in SI units. Let \(m>0\), \(g>0\), \(\varepsilon_{\mathrm{meas}}\ge 0\), and \(\varepsilon_F\ge 0\).

A VTD certificate consists of

\[
\mathrm{VTD}
=
\left(
D,m,g,\widehat a(t^\star),\varepsilon_{\mathrm{meas}},\varepsilon_F
\right),
\]

where

\[
|\widehat a(t^\star)-z''(t^\star)|\le \varepsilon_{\mathrm{meas}}
\]

and

\[
\left|\frac{F_{\mathrm{non\text{-}gravity}}(t^\star)}{m}\right|
\le \varepsilon_F .
\]

## Null model

\[
H_0:\qquad
z''(t^\star)
=
-g+\frac{F_{\mathrm{non\text{-}gravity}}(t^\star)}{m}.
\]

## Anomaly model

\[
H_1:\qquad
z''(t^\star)
=
-g_{\mathrm{eff}}
+
\frac{F_{\mathrm{non\text{-}gravity}}(t^\star)}{m},
\qquad
g_{\mathrm{eff}}\ne g .
\]

## Conditional theorem

If the two certificate bounds above are valid and

\[
|\widehat a(t^\star)+g|
>
\varepsilon_{\mathrm{meas}}+\varepsilon_F,
\]

then \(H_0\) is falsified at \(t^\star\), and

\[
|g_{\mathrm{eff}}-g|
\ge
|\widehat a(t^\star)+g|
-
\varepsilon_{\mathrm{meas}}
-
\varepsilon_F
>
0.
\]

## Proof

Under \(H_0\),

\[
z''(t^\star)+g
=
\frac{F_{\mathrm{non\text{-}gravity}}(t^\star)}{m}.
\]

Therefore

\[
|z''(t^\star)+g|
\le
\varepsilon_F.
\]

Since

\[
|\widehat a(t^\star)-z''(t^\star)|
\le
\varepsilon_{\mathrm{meas}},
\]

the triangle inequality gives

\[
|\widehat a(t^\star)+g|
\le
\varepsilon_{\mathrm{meas}}+\varepsilon_F.
\]

Thus

\[
|\widehat a(t^\star)+g|
>
\varepsilon_{\mathrm{meas}}+\varepsilon_F
\]

contradicts \(H_0\).

Under \(H_1\),

\[
\widehat a(t^\star)+g
=
-(g_{\mathrm{eff}}-g)
+
\frac{F_{\mathrm{non\text{-}gravity}}(t^\star)}{m}
+
e(t^\star),
\]

where

\[
|e(t^\star)|\le \varepsilon_{\mathrm{meas}}.
\]

Hence

\[
|g_{\mathrm{eff}}-g|
\ge
|\widehat a(t^\star)+g|
-
\varepsilon_{\mathrm{meas}}
-
\varepsilon_F.
\]

## Weakest sufficient threshold

Using only the bounds \(\varepsilon_{\mathrm{meas}}\) and \(\varepsilon_F\), the sharp rejection threshold is

\[
\varepsilon_{\mathrm{meas}}+\varepsilon_F.
\]

Any smaller threshold can falsely reject an \(H_0\)-consistent trajectory.

## Claim boundary

The certificate proves only:

\[
\text{ordinary force balance is falsified under the supplied bounds.}
\]

It does not prove:

\[
\text{the physical mechanism is anti-gravity.}
\]

This is a conditional trajectory-anomaly certificate, not a theorem-level URF closure claim.
