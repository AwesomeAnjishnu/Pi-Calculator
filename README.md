From Wikipedia, the free encyclopedia
Part of a series of articles on the
mathematical constant π
3.1415926535897932384626433...
Uses
Area of a circleCircumferenceUse in other formulae
Properties
IrrationalityTranscendence
Value
Less than 22/7ApproximationsMadhava's correction termMemorization
People
ArchimedesLiu HuiZu ChongzhiAryabhataMadhavaJamshīd al-KāshīLudolph van CeulenFrançois VièteSeki TakakazuTakebe KenkoWilliam JonesJohn MachinWilliam ShanksSrinivasa RamanujanJohn WrenchChudnovsky brothersYasumasa Kanada
History
ChronologyA History of Pi
In culture
Indiana Pi BillPi Day
Related topics
Squaring the circleBasel problemSix nines in πOther topics related to π
vte
For other formulas known under the same name, see List of things named after Gottfried Leibniz.
In mathematics, the Leibniz formula for π, named after Gottfried Wilhelm Leibniz, states that

1
−
1
3
+
1
5
−
1
7
+
1
9
−
⋯
=
�
4
,
{\displaystyle 1-{\frac {1}{3}}+{\frac {1}{5}}-{\frac {1}{7}}+{\frac {1}{9}}-\cdots ={\frac {\pi }{4}},}
an alternating series. It is sometimes called the Madhava–Leibniz series as it was first discovered by the Indian mathematician Madhava of Sangamagrama or his followers in the 14th–15th century (see Madhava series),[1] and was later independently rediscovered by James Gregory in 1671 and Leibniz in 1673.[2] The Taylor series for the inverse tangent function, often called Gregory's series, is:

arctan
⁡
�
=
�
−
�
3
3
+
�
5
5
−
�
7
7
+
⋯\arctan x=x-{\frac {x^{3}}{3}}+{\frac {x^{5}}{5}}-{\frac {x^{7}}{7}}+\cdots 
The Leibniz formula is the special case 
arctan
⁡
1
=
1
4
�
.
{\textstyle \arctan 1={\tfrac {1}{4}}\pi .}[3]

It also is the Dirichlet L-series of the non-principal Dirichlet character of modulus 4 evaluated at 
�
=
1
s=1, and, therefore, the value β(1) of the Dirichlet beta function.

Proofs
Proof 1
�
4
=
arctan
⁡
(
1
)
=
∫
0
1
1
1
+
�
2
�
�
=
∫
0
1
(
∑
�
=
0
�
(
−
1
)
�
�
2
�
+
(
−
1
)
�
+
1
�
2
�
+
2
1
+
�
2
)
�
�
=
(
∑
�
=
0
�
(
−
1
)
�
2
�
+
1
)
+
(
−
1
)
�
+
1
(
∫
0
1
�
2
�
+
2
1
+
�
2
�
�
)
.
{\displaystyle {\begin{aligned}{\frac {\pi }{4}}&=\arctan(1)\\&=\int _{0}^{1}{\frac {1}{1+x^{2}}}\,dx\\[8pt]&=\int _{0}^{1}\left(\sum _{k=0}^{n}(-1)^{k}x^{2k}+{\frac {(-1)^{n+1}\,x^{2n+2}}{1+x^{2}}}\right)\,dx\\[8pt]&=\left(\sum _{k=0}^{n}{\frac {(-1)^{k}}{2k+1}}\right)+(-1)^{n+1}\left(\int _{0}^{1}{\frac {x^{2n+2}}{1+x^{2}}}\,dx\right).\end{aligned}}}
Considering only the integral in the last term, we have:

0
≤
∫
0
1
�
2
�
+
2
1
+
�
2
�
�
≤
∫
0
1
�
2
�
+
2
�
�
=
1
2
�
+
3
→
0
 as 
�
→
∞
.
{\displaystyle 0\leq \int _{0}^{1}{\frac {x^{2n+2}}{1+x^{2}}}\,dx\leq \int _{0}^{1}x^{2n+2}\,dx={\frac {1}{2n+3}}\;\rightarrow 0{\text{ as }}n\rightarrow \infty .}
Therefore, by the squeeze theorem, as n → ∞, we are left with the Leibniz series:

�
4
=
∑
�
=
0
∞
(
−
1
)
�
2
�
+
1
{\displaystyle {\frac {\pi }{4}}=\sum _{k=0}^{\infty }{\frac {(-1)^{k}}{2k+1}}}
Proof 2
Let 
�
(
�
)
=
∑
�
=
0
∞
(
−
1
)
�
2
�
+
1
�
2
�
+
1
{\displaystyle f(z)=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{2n+1}}z^{2n+1}}, when 
|
�
|
<
1
|z|<1, the series 
∑
�
=
0
∞
(
−
1
)
�
�
2
�
{\displaystyle \sum _{k=0}^{\infty }(-1)^{k}z^{2k}} to be converges uniformly, then

arctan
⁡
(
�
)
=
∫
0
�
1
1
+
�
2
�
�
=
∑
�
=
0
∞
(
−
1
)
�
2
�
+
1
�
2
�
+
1
=
�
(
�
)
 
(
|
�
|
<
1
)
.
{\displaystyle \arctan(z)=\int _{0}^{z}{\frac {1}{1+t^{2}}}dt=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{2n+1}}z^{2n+1}=f(z)\ (|z|<1).}
Therefore, if 
�
(
�
)
f(z) approaches 
�
(
1
)
f(1) so that it is continuous and converges uniformly, the proof is complete, where, the series 
∑
�
=
0
∞
(
−
1
)
�
2
�
+
1
{\displaystyle \sum _{n=0}^{\infty }{\frac {(-1)^{n}}{2n+1}}} to be converges by the Leibniz's test, and also, 
�
(
�
)
f(z) approaches 
�
(
1
)
f(1) from within the Stolz angle, so from Abel's theorem this is correct.

Convergence

Comparison of the convergence of the Leibniz formula (□) and several historical infinite series for π. Sn is the approximation after taking n terms. Each subsequent subplot magnifies the shaded area horizontally by 10 times. (click for detail)
Leibniz's formula converges extremely slowly: it exhibits sublinear convergence. Calculating π to 10 correct decimal places using direct summation of the series requires precisely five billion terms because 
4
/
2k + 1
 < 10−10 for k > 2 × 1010 − 
1
/
2
 (one needs to apply Calabrese error bound). To get 4 correct decimal places (error of 0.00005) one needs 5000 terms.[4] Even better than Calabrese or Johnsonbaugh error bounds are available.[5]

However, the Leibniz formula can be used to calculate π to high precision (hundreds of digits or more) using various convergence acceleration techniques. For example, the Shanks transformation, Euler transform or Van Wijngaarden transformation, which are general methods for alternating series, can be applied effectively to the partial sums of the Leibniz series. Further, combining terms pairwise gives the non-alternating series

�
4
=
∑
�
=
0
∞
(
1
4
�
+
1
−
1
4
�
+
3
)
=
∑
�
=
0
∞
2
(
4
�
+
1
)
(
4
�
+
3
)
{\displaystyle {\frac {\pi }{4}}=\sum _{n=0}^{\infty }\left({\frac {1}{4n+1}}-{\frac {1}{4n+3}}\right)=\sum _{n=0}^{\infty }{\frac {2}{(4n+1)(4n+3)}}}
which can be evaluated to high precision from a small number of terms using Richardson extrapolation or the Euler–Maclaurin formula. This series can also be transformed into an integral by means of the Abel–Plana formula and evaluated using techniques for numerical integration.

Unusual behaviour
If the series is truncated at the right time, the decimal expansion of the approximation will agree with that of π for many more digits, except for isolated digits or digit groups. For example, taking five million terms yields

3.141592
4
_
5358979323846
4
_
643383279502
7
_
841971693993
873
_
058...
{\displaystyle 3.141592{\underline {4}}5358979323846{\underline {4}}643383279502{\underline {7}}841971693993{\underline {873}}058...}
where the underlined digits are wrong. The errors can in fact be predicted; they are generated by the Euler numbers En according to the asymptotic formula

�
2
−
2
∑
�
=
1
�
2
(
−
1
)
�
−
1
2
�
−
1
∼
∑
�
=
0
∞
�
2
�
�
2
�
+
1
{\displaystyle {\frac {\pi }{2}}-2\sum _{k=1}^{\frac {N}{2}}{\frac {(-1)^{k-1}}{2k-1}}\sim \sum _{m=0}^{\infty }{\frac {E_{2m}}{N^{2m+1}}}}
where N is an integer divisible by 4. If N is chosen to be a power of ten, each term in the right sum becomes a finite decimal fraction. The formula is a special case of the Boole summation formula for alternating series, providing yet another example of a convergence acceleration technique that can be applied to the Leibniz series. In 1992, Jonathan Borwein and Mark Limber used the first thousand Euler numbers to calculate π to 5,263 decimal places with the Leibniz formula.[6]

Euler product
The Leibniz formula can be interpreted as a Dirichlet series using the unique non-principal Dirichlet character modulo 4. As with other Dirichlet series, this allows the infinite sum to be converted to an infinite product with one term for each prime number. Such a product is called an Euler product. It is:

�
4
=
(
∏
�
≡
1
(
mod
4
)
�
�
−
1
)
(
∏
�
≡
3
(
mod
4
)
�
�
+
1
)
=
3
4
⋅
5
4
⋅
7
8
⋅
11
12
⋅
13
12
⋅
17
16
⋅
19
20
⋅
23
24
⋅
29
28
⋯{\displaystyle {\begin{aligned}{\frac {\pi }{4}}&=\left(\prod _{p\equiv 1{\pmod {4}}}{\frac {p}{p-1}}\right)\left(\prod _{p\equiv 3{\pmod {4}}}{\frac {p}{p+1}}\right)\\&={\frac {3}{4}}\cdot {\frac {5}{4}}\cdot {\frac {7}{8}}\cdot {\frac {11}{12}}\cdot {\frac {13}{12}}\cdot {\frac {17}{16}}\cdot {\frac {19}{20}}\cdot {\frac {23}{24}}\cdot {\frac {29}{28}}\cdots \end{aligned}}}
In this product, each term is a superparticular ratio, each numerator is an odd prime number, and each denominator is the nearest multiple of 4 to the numerator.[7]
See also
List of formulae involving π
References
 Plofker, Kim (November 2012), "Tantrasaṅgraha of Nīlakaṇṭha Somayājī by K. Ramasubramanian and M. S. Sriram", The Mathematical Intelligencer, 35 (1): 86–88, doi:10.1007/s00283-012-9344-6, S2CID 124507583
 Roy, Ranjan (1990). "The Discovery of the Series Formula for π by Leibniz, Gregory and Nilakantha" (PDF). Mathematics Magazine. 63 (5): 291–306. doi:10.1080/0025570X.1990.11977541.
Horvath, Miklos (1983). "On the Leibnizian quadrature of the circle" (PDF). Annales Universitatis Scientiarum Budapestiensis (Sectio Computatorica). 4: 75–83.
 Andrews, George E.; Askey, Richard; Roy, Ranjan (1999), Special Functions, Cambridge University Press, p. 58, ISBN 0-521-78988-5
 Villarino, Mark B. (2018-04-21). "The Error in an Alternating Series". The American Mathematical Monthly. 125 (4): 360–364. doi:10.1080/00029890.2017.1416875. hdl:10669/75532. ISSN 0002-9890. S2CID 56124579.
 Rattaggi, Diego (2018-08-30). "Error estimates for the Gregory-Leibniz series and the alternating harmonic series using Dalzell integrals". arXiv:1809.00998 [math.CA].
 Borwein, Jonathan; Bailey, David; Girgensohn, Roland (2004), "1.8.1: Gregory's Series Reexamined", Experimentation in mathematics: Computational paths to discovery, A K Peters, pp. 28–30, ISBN 1-56881-136-5, MR 2051473
 Debnath, Lokenath (2010), The Legacy of Leonhard Euler: A Tricentennial Tribute, World Scientific, p. 214, ISBN 9781848165267.
External links
Leibniz Formula in C, x86 FPU Assembly, x86-64 SSE3 Assembly, and DEC Alpha Assembly
Categories: Pi algorithmsGottfried Wilhelm LeibnizMathematical series
