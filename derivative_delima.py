"""
Command to execute this file:
``` manim -pqh derivative_delima.py main ```
"""
from os import write
from manim import *


class main(Scene):
    def construct(self):
        """Scene 1"""
        title = Text("The Derivative Dilemma", gradient=(RED, BLUE, GREEN), font_size=50)

        subtitle = MathTex(r"{d \over dx} f(x) =\lim_{h \to 0} {f(x+h) - f(x) \over h}",font_size=30, substrings_to_isolate=["x"])
        subtitle.set_color_by_tex_to_color_map({"x": ORANGE})
        subtitle.next_to(title, DOWN)

        credits = Tex("- Mainak Mandal, Arun Pandey", color=TEAL, font_size=20)
        credits.next_to(subtitle, 6 * DOWN)

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

        eqns1 = MathTex(r"a =b", substrings_to_isolate=["a", "b"])
        eqns1.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        self.play(Transform(title, eqns1))
        self.wait(1)
        self.play(ApplyMethod(title.shift, 2 * UP))
        self.wait(2)

        eqns2 = MathTex(r"a^2 =ab", substrings_to_isolate=["a", "b"])
        eqns2.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns2.next_to(title, DOWN)
        self.play(FadeIn(eqns2))
        #  self.play(
        #      TransformMatchingTex(
        #          eqns1.copy(), eqns2,
        #          #  key_map={
        #          #      "C^2": "C",
        #          #      "B^2": "B",
        #          #  }
        #      ),
        #      **play_kw
        #  )
        self.wait(2)

        eqns3 = MathTex(r"a^2-b^2 =ab-b^2", substrings_to_isolate=["a", "b"])
        eqns3.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns3.next_to(eqns2, DOWN)
        #  self.play(FadeIn(eqns3))
        self.play(
            TransformMatchingTex(
                eqns2.copy(), eqns3,
                #  key_map={
                #      "C^2": "C",
                #      "B^2": "B",
                #  }
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

        self.clear()

        """Scene 2"""
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

        """Scene 3"""

        eqns1_s3 = MathTex(r"\frac{d}{dx}x^n = n x^{n-1}", substrings_to_isolate=["x", "n"])
        eqns1_s3.set_color_by_tex_to_color_map({"x": ORANGE,
                                                "n": BLUE})
        self.play(FadeIn(eqns1_s3))
        self.wait(2)
        self.play(FadeOut(eqns1_s3))

        self.clear()

        """Scene 4"""

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

        """ Scene Last"""
        last_text = Tex("Thanks!")
        self.play(FadeIn(last_text))
