# VTD — Conditional Trajectory-Anomaly Certificate

## Definition

Let

\[
D=\{(t_i,z_i)\}_{i=1}^{N},\qquad t_1<\cdots<t_N,
\]

be a vacuum vertical trajectory in SI units. Let \(m>0\), \(g_{\mathrm{cert}}>0\), \(\varepsilon_g\ge 0\), \(\varepsilon_{\mathrm{meas}}\ge 0\), and \(\varepsilon_F\ge 0\).

A VTD certificate consists of

\[
\mathrm{VTD}
=
\left(
D,m,g_{\mathrm{cert}},\varepsilon_g,\widehat a(t^\star),\varepsilon_{\mathrm{meas}},\varepsilon_F
\right),
\]

where

\[
|g_{\mathrm{cert}}-g_{\mathrm{true}}|\le \varepsilon_g,
\]

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
-g_{\mathrm{true}}+\frac{F_{\mathrm{non\text{-}gravity}}(t^\star)}{m}.
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
g_{\mathrm{eff}}\ne g_{\mathrm{true}} .
\]

## Conditional theorem

If the two certificate bounds above are valid and

\[
|\widehat a(t^\star)+g_{\mathrm{cert}}|
>
\varepsilon_{\mathrm{meas}}+\varepsilon_F+\varepsilon_g,
\]

then \(H_0\) is falsified at \(t^\star\), and

\[
|g_{\mathrm{eff}}-g_{\mathrm{true}}|
\ge
|\widehat a(t^\star)+g_{\mathrm{cert}}|
-
\varepsilon_{\mathrm{meas}}
-
\varepsilon_F
-
\varepsilon_g
>
0.
\]

## Proof

Under \(H_0\),

\[
z''(t^\star)+g_{\mathrm{true}}
=
\frac{F_{\mathrm{non\text{-}gravity}}(t^\star)}{m}.
\]

Therefore

\[
|z''(t^\star)+g_{\mathrm{cert}}|
\le
\varepsilon_F+\varepsilon_g.
\]

Since

\[
|\widehat a(t^\star)-z''(t^\star)|
\le
\varepsilon_{\mathrm{meas}},
\]

the triangle inequality gives

\[
|\widehat a(t^\star)+g_{\mathrm{cert}}|
\le
\varepsilon_{\mathrm{meas}}+\varepsilon_F+\varepsilon_g.
\]

Thus

\[
|\widehat a(t^\star)+g_{\mathrm{cert}}|
>
\varepsilon_{\mathrm{meas}}+\varepsilon_F+\varepsilon_g
\]

contradicts \(H_0\).

Under \(H_1\),

\[
\widehat a(t^\star)+g_{\mathrm{cert}}
=
-(g_{\mathrm{eff}}-g_{\mathrm{true}})+(g_{\mathrm{cert}}-g_{\mathrm{true}})
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
|g_{\mathrm{eff}}-g_{\mathrm{true}}|
\ge
|\widehat a(t^\star)+g_{\mathrm{cert}}|
-
\varepsilon_{\mathrm{meas}}
-
\varepsilon_F
-
\varepsilon_g.
\]

## Weakest sufficient threshold

Using only the bounds \(\varepsilon_{\mathrm{meas}}\), \(\varepsilon_F\), and \(\varepsilon_g\), the sharp rejection threshold is

\[
\varepsilon_{\mathrm{meas}}+\varepsilon_F+\varepsilon_g.
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
