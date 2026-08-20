# Mensuration

> CAT quant. Unlike plane geometry, this really is a formula topic — but the questions are almost never "apply one formula". They are **volume conservation**, **which faces disappear**, and **scaling**. Get those three reflexes and the formula table becomes lookup.

---

## 1. The solid formula table

| Solid | Volume | Curved / lateral SA | Total SA |
|---|---|---|---|
| Cube (edge a) | a³ | 4a² | **6a²** |
| Cuboid (l, b, h) | lbh | 2h(l + b) | 2(lb + bh + hl) |
| Cylinder | πr²h | 2πrh | 2πr(r + h) |
| Cone | **⅓**πr²h | πrl | πr(r + l) |
| Sphere | (4/3)πr³ | — | **4πr²** |
| Hemisphere | (2/3)πr³ | 2πr² | **3πr²** |
| Prism | base area × h | perimeter × h | + 2 × base |
| Pyramid | ⅓ × base area × h | ½ × perimeter × slant | + base |

- **Cone slant** l = √(r² + h²). The 3-4-5 and 5-12-13 triples show up here constantly.
- **Diagonal** of a cuboid = √(l² + b² + h²); of a cube = a√3
- The ⅓ appears exactly where there is an apex — cone and pyramid. Cylinder and prism have none.

**Numbers worth having ready** (π = 22/7): a cylinder of r = 7, h = 10 has CSA 440; a cone of r = 7, h = 12 has volume 616; a sphere of r = 6 has volume 288π.

**Cone : sphere : cylinder** of the same radius and the same height 2r stand in the ratio **1 : 2 : 3**. Worth memorising outright — it answers several questions on its own.

---

## 2. The scaling rule

Scale every linear dimension by k:

- **lengths × k, areas × k², volumes × k³**

Half of all CAT mensuration questions are only this. Read backwards it is just as useful: volumes in the ratio 8 : 27 ⟹ radii in the ratio **2 : 3** ⟹ surface areas **4 : 9**.

**Worked example:** Two spheres have radii in the ratio 2 : 3. Their surface areas are in ratio **4 : 9**, their volumes **8 : 27**.

**The trap this exists to catch:** scaling a volume by k when it should be k³, or by k² because "area" was mentioned somewhere in the question.

---

## 3. Type 1 — Recasting and volume conservation

**The single most common mensuration question type.** Metal is melted, water is poured, wire is drawn — and

**volume is conserved. Surface area is not.**

**Method:** write V(before) = V(after), cancel π and every common factor before touching a calculator, and solve.

**Worked example:** A solid sphere of radius 6 is melted and recast into spheres of radius 2. How many?
- Volumes scale as r³ ⟹ (6/2)³ = **27**. No π, no 4/3, no arithmetic.

**Worked example (shape changes):** A cylinder of radius 6 and height 15 is recast into cones of radius 3 and height 5. How many?
- Cylinder = π·36·15 = 540π; cone = ⅓·π·9·5 = 15π ⟹ **36 cones**

**Worked example (wire drawing):** A cube of edge 6 cm is drawn into a wire of radius 1 mm. Find the length.
- 216 = π(0.1)²·L ⟹ L = 216/(0.01π) = 21600/π ≈ **6875 cm**
- Note the unit change — mm to cm — which is where these are usually lost.

**When shapes are geometrically similar, skip the formula entirely** and use the cube of the linear ratio. When they aren't (sphere → cone), you must write both volumes.

**The paired trap:** a question that melts a sphere into a cube and asks for the **surface area** of the result. You conserve volume to get the edge, then compute the new surface area from scratch. Surface area is never conserved and the two are almost never equal.

---

## 4. Type 2 — Combined solids and the faces that disappear

When two solids are joined, **volumes add** but **surface areas do not** — the two faces in contact vanish from the exterior.

**Method:**
1. Add the volumes. That part is safe.
2. For surface area, list the exposed surfaces one at a time and **never** add two total surface areas.

| Combination | Exposed surface |
|---|---|
| Cone on a cylinder (same r) | πrl + 2πrh + πr² (one base only) |
| Hemisphere on a cylinder | 2πr² + 2πrh + πr² |
| Hemisphere scooped **out** of a cylinder's top | 2πr² + 2πrh + πr² — the same, since a dent adds as much as it removes |
| Two cubes of edge a joined face to face | 12a² − 2a² = **10a²** |
| Sphere resting in a hemispherical bowl | contact is a point/circle — nothing vanishes |

**Worked example:** A toy is a cone of radius 7 and slant 25 mounted on a hemisphere of radius 7. Find the total surface area (π = 22/7).
- Cone curved = πrl = (22/7)(7)(25) = 550
- Hemisphere curved = 2πr² = 2(22/7)(49) = 308
- The cone's base and the hemisphere's flat face are both internal ⟹ excluded
- Total = **858**

**The reliable habit:** draw the joined solid and shade what a hand would touch. Anything unshaded is not in the answer.

---

## 5. Type 3 — Hollow solids, pipes and shells

Everything hollow is **outer minus inner**.

- **Pipe / hollow cylinder:** volume of material = π(R² − r²)h; total SA = 2πh(R + r) + 2π(R² − r²)
- **Spherical shell:** volume = (4/3)π(R³ − r³)
- **Open box / tank:** subtract the missing face when computing surface area — an open cuboid tank has SA = lb + 2h(l + b), not 2(lb + bh + hl)

**Worked example:** A pipe has outer radius 5, inner radius 4 and length 14. Volume of metal?
- π(25 − 16)(14) = 126π

**The trap:** treating the thickness t as the inner radius. If the outer radius is R and the thickness is t, the inner radius is **R − t**, and R² − r² = t(2R − t) — not t².

---

## 6. Frustum, and cones cut parallel to the base

A cone cut by a plane parallel to its base at a height ratio k **from the apex** produces a small cone similar to the original with ratio k, so:

- small cone volume = **k³** × original
- the frustum takes the remaining **(1 − k³)**

**Frustum formulas** (radii R and r, height h):

- **Volume = (πh/3)(R² + Rr + r²)**
- Slant l = √(h² + (R − r)²); **curved SA = πl(R + r)**; total adds πR² + πr²

**Worked example:** A cone is cut halfway up. Find the ratio of the small cone to the frustum.
- Halfway from the apex means k = ½ ⟹ small cone = ⅛ ⟹ frustum = ⅞ ⟹ ratio **1 : 7**

That 1 : 7 is worth memorising; "halfway up" is by far the most common cut, and the intuitive answer of 1 : 1 is planted in the options.

---

## 7. Type 4 — The painted cube

A cube is painted on all six faces, then cut into **n³** unit cubes. Then:

| Faces painted | Count | Where they are |
|---|---|---|
| **3** | **8** | the corners — always 8, independent of n |
| **2** | **12(n − 2)** | the edges, excluding corners |
| **1** | **6(n − 2)²** | the face interiors |
| **0** | **(n − 2)³** | the hidden inner cube |

The four counts sum to n³ — that is just the expansion of ((n − 2) + 2)³, and it is the check to run before answering.

**Worked example:** A cube is cut into 125 smaller cubes. How many have exactly two faces painted?
- n = 5 ⟹ 12(3) = **36**. (Check: 8 + 36 + 6·9 = 8 + 36 + 54 = 98 painted, plus 27 unpainted = 125 ✓)

**The variants CAT uses:**
- **Only some faces painted** — recount by position rather than reaching for the formula; the formula assumes all six.
- **Two colours** on opposite face pairs — count cubes carrying each colour combination separately.
- **A cuboid** cut into l × b × h unit cubes: unpainted = (l−2)(b−2)(h−2), exactly one face = 2[(l−2)(b−2) + (b−2)(h−2) + (h−2)(l−2)], two faces = 4[(l−2) + (b−2) + (h−2)], three faces = 8.

**n = 2 is degenerate:** every one of the 8 cubes has 3 faces painted, and the formulas correctly give 12(0) = 0 and (0)³ = 0.

---

## 8. Type 5 — Cutting a solid with a plane

**Check whether it is a *prism* cut before computing anything.**

If every marked point on the top face lies **directly above** its partner on the bottom face, the plane is **vertical**. Both pieces are prisms of the solid's full height, so

**volume ratio = area ratio of the cross-section on the top face**

The 3-D problem collapses to a 2-D one.

**How to spot it:** the marked points come in pairs on *corresponding* edges of the two horizontal faces, dividing them in the same ratio. "A on SP and D on ZW with SA : AP = ZD : DW" is exactly that signal.

**Worked example:** A cube is cut by plane ABCD. A on SP and D on ZW with SA : AP = ZD : DW = 1 : 2; B and C bisect PQ and WX. Find (larger part) : (whole).
- A is above D, B above C ⟹ vertical plane ⟹ work on the top face alone.
- Take the side as 3. S(0,0), P(3,0), Q(3,3), R(0,3) ⟹ A = (1, 0), B = (3, 1.5)
- AB cuts off right triangle APB, legs 2 and 1.5 ⟹ area 1.5 of 9
- Larger piece = 7.5/9 = **5/6**

**When the cut is not vertical** you are usually looking at a corner tetrahedron or a wedge — use ⅓ × base × height, or subtract the tetrahedron from the whole.

---

## 9. Type 6 — Unfolding: shortest path across a surface

An ant crawling **on the surface** cannot use the interior diagonal. **Flatten the surface into a plane** and the shortest path becomes a straight line.

**Cuboid, opposite corners:** unfolding gives three candidates, √(l² + (b + h)²) and its two permutations. The minimum comes from **pairing the two smallest dimensions together** inside the bracket.

**Worked example:** A box is 8 × 6 × 5. Shortest surface path between opposite corners?
- Candidates: √(8² + 11²) = √185, √(6² + 13²) = √205, √(5² + 14²) = √221
- Minimum = **√185 ≈ 13.6** — the pairing that adds the two smallest, 6 and 5, against the largest
- Compare the space diagonal √(64 + 36 + 25) = √125 ≈ 11.2, which the ant cannot use — and which is the planted decoy

**Cylinder:** unroll the curved surface into a rectangle of width 2πr and height h. A spiral of one full turn becomes the hypotenuse √(h² + (2πr)²); n turns give √(h² + (2πnr)²).

---

## 10. Inscribed and circumscribed solids

| Configuration | Relation |
|---|---|
| Sphere inscribed in a cube of edge a | r = **a/2** |
| Cube inscribed in a sphere of radius R | a√3 = 2R ⟹ a = **2R/√3** |
| Sphere inscribed in a cylinder (h = 2r) | volumes **2 : 3**, curved surfaces **equal** |
| Cone, hemisphere, cylinder — same r, height r | volumes **1 : 2 : 3** |
| Largest cone inside a cube of edge a | r = a/2, h = a |
| Largest sphere inside a cone (r, h) | radius = rh / (r + l), where l is the slant |

The sphere-in-cylinder result (Archimedes) is the one CAT reuses: the sphere is exactly two-thirds of its circumscribing cylinder, in both volume and curved surface area.

---

## 11. Type 7 — Liquid level and immersion

- **Dropping a solid into a cylinder:** the level rises by V(solid) / πr², provided the object is fully submerged and does not float
- **Pouring between containers:** volume is conserved; only the shape of the free surface changes
- **A partially filled cone, apex down:** the liquid forms a similar cone, so a fill height of ratio k gives a volume ratio **k³**. Half the height is one-eighth the volume, not half.
- **Emptying/filling rates** belong to `11-Time-Work-Pipes-Cisterns.md` §7 — this section is only about the geometry

**Worked example:** A sphere of radius 3 is dropped into a cylinder of radius 6 containing water. By how much does the level rise?
- Sphere volume = 36π; rise = 36π / (36π) = **1 unit**

**Worked example (the cone trap):** An inverted cone is filled to half its height. What fraction of its capacity is that?
- k = ½ ⟹ **1/8**, not ½

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Volume scaling | × k | × k³ (areas × k²) |
| Recasting | equate surface areas | equate **volumes**; SA is not conserved |
| Combined solids | add both total surface areas | the joined faces vanish |
| Cone volume | πr²h | **⅓**πr²h |
| Hemisphere total SA | 2πr² | 3πr² — the flat face counts |
| Cone slant | equals the height | l = √(r² + h²) |
| Pipe thickness t | inner radius = t | inner radius = R − t |
| Cone cut halfway | pieces are 1 : 1 | **1 : 7** |
| Painted cube, 2 faces | 12n | 12(n − 2) |
| Ant on a box | space diagonal | unfold the surface; √(l² + (b+h)²), two smallest paired |
| Cone half-filled by height | half the volume | one-eighth |
| Open tank | 2(lb + bh + hl) | subtract the missing face |
| Units | mixed mm and cm | convert before writing the equation |

---

## Practical exam habits

- Write the conservation equation before any numbers. "Volume before = volume after" is the whole method for a third of this topic.
- Cancel π and common factors symbolically first. Most mensuration arithmetic errors happen in numbers that were going to cancel anyway.
- If the radius is a multiple of 7, use π = 22/7 — the setter chose it so the answer is clean.
- For any combined solid, shade what a hand would touch before computing surface area.
- For similar shapes, never touch a formula. Go straight to k, k², k³.
- Check the units line in the question. Mensuration is where CAT hides mm-versus-cm more than anywhere else.

**Where this feeds forward:** `17-Triangles.md` §3 (triples appear in every cone slant), `18-Circles.md` §1 (every cross-section is a circle or a sector), `19-Quadrilaterals-and-Polygons.md` §6 (prism and pyramid bases), `02-Percentages.md` §5 (a % change in a dimension cubes for volume), `23-PnC-Probability.md` (the painted-cube counts are positional counting).
