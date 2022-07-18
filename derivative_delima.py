"""
Command to execute this file:
``` manim -pqh derivative_delima.py main ```

Note: The scene # below does not correspond to the scene # in script.
Use your discretion.
"""
from os import write
from manim import *
from numpy.core.multiarray import arange


class main(Scene):
    def construct(self):
        """Scene """
        title = Text("The Derivative Dilemma", gradient=(RED, BLUE, GREEN), font_size=50)
        title.move_to(UP)

        subtitle = MathTex(r"{d \over dx} f(x) =\lim_{h \to 0} {f(x+h) - f(x) \over h}",font_size=30, substrings_to_isolate=["x"])
        subtitle.set_color_by_tex_to_color_map({"x": ORANGE})
        subtitle.next_to(title, 1.5 * DOWN)

        credits = Tex("- Mainak Mandal, Arun Pandey", color=TEAL, font_size=20)
        credits.next_to(subtitle, 7 * DOWN)

        framebox1 = SurroundingRectangle(subtitle, buff=.1)
        framebox1.set_stroke(width=1)

        self.play(
            Write(title),
            FadeIn(subtitle, shift=UP),
            Create(framebox1),
            FadeIn(credits)
        )
        self.wait(3)
        self.play(FadeOut(framebox1, shift=DOWN),
                  FadeOut(subtitle, shift=DOWN),
                  FadeOut(credits, shift=DOWN))

        play_kw = {"run_time": 2}

        """ Scene """
        pg_title = Text("Prelude", font_size=25, color=TEAL)
        pg_title.shift(3*UP)
        pg_title.shift(5*LEFT)


        eqns1 = MathTex(r"a =b", substrings_to_isolate=["a", "b"])
        eqns1.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        self.play(Transform(title, eqns1), FadeIn(pg_title))
        self.wait(1)
        self.play(ApplyMethod(title.shift, 2 * UP))
        self.wait(2)

        eqns2 = MathTex(r"a^2 =ab", substrings_to_isolate=["a", "b"])
        eqns2.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns2.next_to(title, DOWN)
        self.play(FadeIn(eqns2))
        self.wait(2)

        eqns3 = MathTex(r"a^2-b^2 =ab-b^2", substrings_to_isolate=["a", "b"])
        eqns3.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns3.next_to(eqns2, DOWN)
        self.play(
            TransformMatchingTex(
                eqns2.copy(), eqns3,
            ),
            **play_kw
        )
        self.wait(2)

        eqns4 = MathTex(r"(a+b)(a-b) =b(a-b)", substrings_to_isolate=["a", "b"])
        eqns4.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns4.next_to(eqns3, DOWN)
        self.play(
            TransformMatchingTex(
                eqns3.copy(), eqns4,
            ),
            **play_kw
        )
        self.wait(2)

        eqns5 = MathTex(r"2b(a-b) =b(a-b)", substrings_to_isolate=["a", "b"])
        eqns5.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns5.next_to(eqns4, DOWN)
        self.play(
            TransformMatchingTex(
                eqns4.copy(), eqns5,
            ),
            **play_kw
        )
        self.wait(2)

        eqns6 = MathTex(r"2b =b", substrings_to_isolate=["a", "b"])
        eqns6.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns6.next_to(eqns5, DOWN)
        #  self.play(FadeIn(eqns6))
        self.play(
            TransformMatchingTex(
                eqns5.copy(), eqns6,
                key_map={
                    "2b": "b",
                    "b": "b",
                }
            ),
            **play_kw
        )
        self.wait(2)

        eqns7 = MathTex(r"2 =1~\text{!}")
        eqns7.next_to(eqns6, DOWN)
        #  self.play(FadeIn(eqns7))
        self.play(
            TransformMatchingTex(
                eqns6.copy(), eqns7,
                key_map={
                    "2": "1",
                    "1": "1",
                }
            ),
            **play_kw
        )
        self.wait(2)

        self.play(
                  FadeOut(title),
                  FadeOut(eqns2),
                  FadeOut(eqns3),
                  FadeOut(eqns4),
                  FadeOut(eqns5),
                  FadeOut(eqns6),
                  FadeOut(eqns7)
                  )

        """Scene """

        eqns1_s2 = MathTex(r"a \times b =", r"a + a + a + \ldots + a", substrings_to_isolate=["a", "b"])
        eqns1_s2.set_color_by_tex_to_color_map({"a": YELLOW,
                                                "b": RED})
        Bi = Brace(eqns1_s2[4:], UP)
        ti = Bi.get_tex(r"(", r"b", r"~ \mathrm{times})")
        ti[1].set_color(RED)

        grp = VGroup(eqns1_s2,Bi,ti)
        self.play(FadeIn(eqns1_s2))
        self.play(FadeIn(Bi,ti))
        self.play(ApplyMethod(grp.shift, 2 * UP))
        self.wait(2)

        eqns2_s2 = MathTex(r"2^2 = 2+2", substrings_to_isolate=["a", "b"])
        eqns2_s2.next_to(eqns1_s2, 3 * DOWN)
        eqns2_s2.set_color_by_tex_to_color_map({"a": YELLOW,
                                                "b": RED,
                                                "x": ORANGE})
        self.play(FadeIn(eqns2_s2))
        self.wait(2)

        eqns2_s3 = MathTex(r"3^2 =3+3+3", substrings_to_isolate=["a", "b"])
        eqns2_s3.next_to(eqns2_s2, DOWN)
        eqns2_s3.set_color_by_tex_to_color_map({"a": YELLOW,
                                                "b": RED,
                                                "x": ORANGE})
        self.play(FadeIn(eqns2_s3))
        self.wait(2)

        eqns2_s4 = MathTex(r" x^2 = x +x + x \ldots + x", substrings_to_isolate=["x"])
        eqns2_s4.next_to(eqns2_s3, DOWN)
        eqns2_s4.set_color_by_tex_to_color_map({"x": ORANGE})

        Bi = Brace(eqns2_s4[3:], DOWN)
        ti = Bi.get_tex(r"(", r"x", r"~ \mathrm{times})")
        ti[1].set_color(ORANGE)

        grp = VGroup(Bi,ti)

        self.play(FadeIn(eqns2_s4))
        self.play(FadeIn(grp))
        self.wait(2)

        self.clear()

        """Scene """

        eqns1_s3 = MathTex(r"\frac{d}{dx}x^n = n x^{n-1}", substrings_to_isolate=["x", "n"])
        eqns1_s3.set_color_by_tex_to_color_map({"x": ORANGE,
                                                "n": BLUE})
        self.play(FadeIn(eqns1_s3))
        self.wait(2)
        self.play(FadeOut(eqns1_s3))

        self.clear()

        """Scene """

        eqns1_s4 = MathTex(r"\frac{d}{dx}x^2 =", r"\frac{d}{dx}(x +x + x + \ldots + x)", substrings_to_isolate=["x"])
        eqns1_s4.set_color_by_tex_to_color_map({"x": ORANGE})

        Bi = Brace(eqns1_s4[7:], UP)
        ti = Bi.get_tex(r"(", r"x", r"~ \mathrm{times})")
        ti[1].set_color(ORANGE)

        grp = VGroup(eqns1_s4, Bi,ti)

        self.play(FadeIn(eqns1_s4))
        self.play(FadeIn(Bi,ti))
        self.play(ApplyMethod(grp.shift, 2 * UP))
        self.wait(2)

        eqns2_s4 = MathTex(r"{{2x= \frac{d}{dx}x + \frac{d}{dx}x + \frac{d}{dx}x + \ldots \quad (x}}~\mathrm{times})",
                           substrings_to_isolate=["x"])
        eqns2_s4.next_to(eqns1_s4, DOWN)
        eqns2_s4.set_color_by_tex_to_color_map({"x": ORANGE})
        self.play(FadeIn(eqns2_s4))
        self.wait(2)

        eqns3_s4 = MathTex(r"{{2x =1 + 1 + 1 + \ldots \quad (x~}} \mathrm{times})", substrings_to_isolate=["x"])
        eqns3_s4.next_to(eqns2_s4, DOWN)
        eqns3_s4.set_color_by_tex_to_color_map({"x": ORANGE})
        self.play(FadeIn(eqns3_s4))
        self.wait(2)

        eqns4_s4 = MathTex(r"2x=x", substrings_to_isolate=["a", "b", "x"])
        eqns4_s4.next_to(eqns3_s4, DOWN)
        eqns4_s4.set_color_by_tex_to_color_map({"a": YELLOW,
                                                "b": RED,
                                                "x": ORANGE})
        self.play(FadeIn(eqns4_s4))
        self.wait(2)

        self.clear()

        """ Scene """

        equation = MathTex(r"f(x)=x^2", font_size=30, substrings_to_isolate=["x"])
        equation.move_to(2.5*UP)
        equation.set_color_by_tex_to_color_map({"x": ORANGE})

        ax = Axes(
            x_range=[0, 4, 0.5],
            y_range=[0, 16, 1],
            axis_config={"include_tip": False,
                         "include_numbers": True}
        )
        labels = ax.get_axis_labels(x_label="x",
                                    y_label="f(x)")
        curve_1 = ax.plot(lambda x: x ** 2, x_range=[0, 4], color=BLUE_C)
        grp1 = Group(ax, labels, curve_1)
        grp1.scale(0.45)
        grp1.move_to(3.5*LEFT)

        ax2 = Axes(
            x_range=[0, 4, 0.5],
            y_range=[0, 16, 1],
            axis_config={"include_tip": False,
                         "include_numbers": True}
        )
        labels2 = ax2.get_axis_labels(x_label="x",
                                    y_label="f(x)")
        x_pts = [x for x in arange(0, 4.5, 0.5)]
        y_pts = [x*x for x in arange(0, 4.5, 0.5)]
        curve_2 = ax2.plot_line_graph(x_values=x_pts, y_values=y_pts, line_color=BLUE_C)


        grp2 = Group(ax2, labels2, curve_2["vertex_dots"])
        grp2.scale(0.45)
        grp2.move_to(3.5*RIGHT)

        equation2 = MathTex(r"{d \over dx} f(x) =\lim_{h \to 0} {f(x+h) - f(x) \over h}",font_size=30, substrings_to_isolate=["x"])
        equation2.set_color_by_tex_to_color_map({"x": ORANGE})
        equation2.move_to(2.5*DOWN)

        self.play(Write(equation))
        self.play(FadeIn(grp1), FadeIn(grp2))
        self.play(Write(equation2))

        self.wait(2)

        self.clear()

        """ Scene """
        eq1 = MathTex(r"x^2 =x+x+\cdots+x + (x-\lfloor x \rfloor) \cdot x", substrings_to_isolate=["x"])
        eq1.set_color_by_tex_to_color_map({"x": ORANGE})
        eq1.move_to(3*UP)

        Bi = Brace(eq1[2:7], DOWN)
        ti = Bi.get_tex(r"\lfloor", r"x", r"\rfloor \mathrm{~times}")
        ti[1].set_color(ORANGE)

        grp = VGroup(eq1, Bi,ti)

        eq2 = MathTex(r"\frac{d}{dx}(xf(x)) =1\cdot f(x) + x \cdot {d \over dx} f(x)", substrings_to_isolate=["x"])
        eq2.set_color_by_tex_to_color_map({"x": ORANGE})
        eq2.next_to(grp, 2*DOWN)

        eq3 = MathTex(r"{d \over dx}(x \cdot x) ={dx \over dx} \cdot x + x \cdot {dx \over dx}", substrings_to_isolate=["x"])
        eq3.set_color_by_tex_to_color_map({"x": ORANGE})
        eq3.next_to(eq2, DOWN)

        eq4 = MathTex(r"\frac{d}{dx}(x \cdot x) =2x", substrings_to_isolate=["x"])
        eq4.set_color_by_tex_to_color_map({"x": ORANGE})
        eq4.next_to(eq3, DOWN)

        self.play(FadeIn(grp))
        self.play(FadeIn(eq2))
        self.play(FadeIn(eq3))
        self.play(FadeIn(eq4))

        self.wait(2)

        self.play(FadeOut(grp),
                  FadeOut(eq2),
                  FadeOut(eq3),
                  FadeOut(eq4))

        """ Scene Last"""
        last_text = Tex("Thanks!")
        self.play(FadeIn(last_text))

