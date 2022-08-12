"""
Command to execute this file:
``` manim -pqh derivative_delimma.py main ```
"""
from manim import *
from numpy.core.multiarray import arange
import math

def PDF_normal(x, mu, sigma):
    ''' General form of probability density function of univariate normal distribution '''
    return math.exp(-((x-mu)**2)/(2*sigma**2))/(sigma*math.sqrt(2*math.pi))

class main(Scene):

    def construct(self):
        title, pg_title = self.intro_scene()

        self.next_section()
        self.scene_2(title=title, pg_title=pg_title)

        self.next_section()
        self.scene_3(title=title)

        self.next_section()
        self.scene_4(pg_title=pg_title)

        self.next_section()
        self.scene_5()

        self.next_section()
        self.scene_6()

        self.next_section()
        self.scene_7()

        self.next_section()
        self.scene_thanks()

    def intro_scene(self):
        title = Text("The Derivative Dilemma", gradient=(RED, BLUE, GREEN), font_size=50)
        title.shift(3*UP)

        subtitle = MathTex(r"{d \over dx} f(x) =\lim_{h \to 0} {f(x+h) - f(x) \over h}",font_size=30, substrings_to_isolate=["x"])
        subtitle.set_color_by_tex_to_color_map({"x": ORANGE})
        subtitle.next_to(title, 1.5 * DOWN)

        framebox1 = SurroundingRectangle(subtitle, buff=.1)
        framebox1.set_stroke(width=1)


        pg_title = Text("Introduction", font_size=25, color=TEAL)
        pg_title.shift(3*UP)
        pg_title.shift(5*LEFT)

        ax = Axes(
            x_range = [-4, 5, 1],
            y_range = [0, 0.5, 0.1],
            axis_config = {'include_numbers':True}
        )
        labels = ax.get_axis_labels(x_label="x",
                                    y_label="f(x)")

        curve = always_redraw(lambda: ax.plot(lambda x: PDF_normal(x, 0, 1)))

        alpha = ValueTracker(0.4)  # this is the value we're changing when animating

        # function for drawing the tangent line
        draw_tangent = (lambda: TangentLine(curve, alpha.get_value(), 2, color=YELLOW))

        # always redraw the tangent line, i.e. update when alpha changes
        tangent = always_redraw(draw_tangent)

        grp1 = Group(ax, labels, curve, tangent)
        grp1.scale(0.40)
        grp1.next_to(subtitle, DOWN)


        credits = Tex("- Mainak Mandal, Arun Pandey", color=TEAL, font_size=20)
        credits.next_to(curve, 4 * DOWN)


        self.wait(1)
        self.play(
            Write(title),
            run_time=2,
        )
        self.wait(5)
        self.play(
            Write(subtitle),
            Create(framebox1),
            run_time=2,
        )
        self.wait(4)
        self.play(
            Create(ax),
            Create(labels),
            Create(curve),
            run_time=3
        )
        self.wait(1)
        self.play(Create(tangent))
        #  # move the value of alpha around
        for alpha_ in (0.3, 0.2, 0.5, 0.8):
            self.play(alpha.animate.set_value(alpha_))

        self.wait(6)
        self.play(
            FadeIn(credits)
        )
        self.wait(3)

        self.play(FadeOut(framebox1, shift=DOWN),
                  FadeOut(grp1, shift=DOWN),
                  FadeOut(subtitle, shift=DOWN),
                  FadeOut(credits, shift=DOWN))
        return title, pg_title

    def scene_2(self, title: Mobject, pg_title: Mobject):
        eqns0 = MathTex(r"1", r"\times", r"0", r"=", r"2", r"\times", r"0")
        eqns0.shift(UP)
        self.play(Transform(title, eqns0), FadeIn(pg_title))
        self.wait(4)

    def scene_3(self, title: Mobject):
        eqns1 = MathTex(r"a", r"=", r"b", substrings_to_isolate=["a", "b"])
        eqns1.shift(UP)
        eqns1.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        self.play(Transform(title, eqns1))
        self.play(ApplyMethod(title.shift, UP))
        self.wait(4)

        eqns2 = MathTex(r"a", r"^2", r"=", r"a", r"b", substrings_to_isolate=["a", "b"])
        eqns2.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns2.next_to(title, DOWN)
        self.play(
            ReplacementTransform(title[6].copy(), eqns2[:2]),
            ReplacementTransform(title[13].copy(), eqns2[2]),
            ReplacementTransform(title[19].copy(), eqns2[3:]),
            run_time=1.5
        )
        self.wait(6)

        eqns3 = MathTex(r"a",
                        r"^2",
                        r"-",
                        r"b",
                        r"^2",
                        r" =",
                        r"a",
                        r"b",
                        r"-",
                        r"b",
                        r"^2",
                        substrings_to_isolate=["a", "b"])
        eqns3.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns3.next_to(eqns2, DOWN)
        self.play(
            TransformMatchingTex(eqns2.copy(), eqns3),
            run_time=1.5
        )
        self.wait(7)

        eqns4 = MathTex(r"(a+b)(a-b) =b(a-b)", substrings_to_isolate=["a", "b"])
        eqns4.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns4.next_to(eqns3, DOWN)
        self.play(
            TransformMatchingTex(eqns3.copy(), eqns4),
            run_time=1.5
        )
        self.wait(6)

        eqns5 = MathTex(r"2b", r"(a-b)", r"=", r"b", r"(a-b)", substrings_to_isolate=["a", "b"])
        eqns5.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns5.next_to(eqns4, DOWN)
        self.play(
            ReplacementTransform(eqns4[:5].copy(), eqns5[:3]),
            ReplacementTransform(eqns4[5:10].copy(), eqns5[3:8]),
            ReplacementTransform(eqns4[11].copy(), eqns5[8]),
            ReplacementTransform(eqns4[12:].copy(), eqns5[9:]),
            run_time=1.5
        )
        self.wait(12)

        eqns6 = MathTex(r"2b", r"=", r"b", substrings_to_isolate=["a", "b"])
        eqns6.set_color_by_tex_to_color_map({"a": YELLOW,
                                             "b": RED,
                                             "x": ORANGE})
        eqns6.next_to(eqns5, DOWN)
        self.play(
            ReplacementTransform(eqns5[:2].copy(), eqns6[:2]),
            ReplacementTransform(eqns5[7].copy(), eqns6[2]),
            ReplacementTransform(eqns5[8].copy(), eqns6[3]),
            run_time=1.5
        )
        self.wait(6)

        eqns7 = MathTex(r"2", r"=", r"1")
        eqns7.next_to(eqns6, DOWN)
        self.play(
            ReplacementTransform(eqns6[0].copy(), eqns7[0]),
            ReplacementTransform(eqns6[2].copy(), eqns7[1]),
            ReplacementTransform(eqns6[3].copy(), eqns7[2]),
            run_time=1.5
        )

        warn_txt = Tex("!!")
        warn_txt.set_color(RED)
        warn_txt.next_to(eqns7, RIGHT)
        self.play(Write(warn_txt))
        self.wait(22)

        self.play(
            FadeOut(title),
            FadeOut(eqns2),
            FadeOut(eqns3),
            FadeOut(eqns4),
            FadeOut(eqns5),
            FadeOut(eqns6),
            FadeOut(eqns7),
            FadeOut(warn_txt)
        )

    def scene_4(self, pg_title: Mobject):
        eqns1_s2 = MathTex(r"a \times b =", r"a + a + a + \cdots + a", substrings_to_isolate=["a", "b"])
        eqns1_s2.shift(UP)
        eqns1_s2.set_color_by_tex_to_color_map({"a": YELLOW,
                                                "b": RED})
        Bi1 = Brace(eqns1_s2[4:], UP)
        ti1 = Bi1.get_tex(r"(", r"b", r"~ \mathrm{times})")
        ti1[1].set_color(RED)

        grp1 = VGroup(eqns1_s2,Bi1,ti1)
        self.play(FadeIn(eqns1_s2[:4]))
        self.play(Write(eqns1_s2[4:]))
        self.play(FadeIn(Bi1,ti1))
        self.play(ApplyMethod(grp1.shift, UP))
        self.wait(6)

        eqns2_s2 = MathTex(r"2^2 = 2+2", substrings_to_isolate=["a", "b"])
        eqns2_s2.next_to(eqns1_s2, 3 * DOWN)
        eqns2_s2.set_color_by_tex_to_color_map({"a": YELLOW,
                                                "b": RED,
                                                "x": ORANGE})
        self.play(FadeIn(eqns2_s2))
        self.wait(3)

        eqns2_s3 = MathTex(r"3^2 =3+3+3", substrings_to_isolate=["a", "b"])
        eqns2_s3.next_to(eqns2_s2, DOWN)
        eqns2_s3.set_color_by_tex_to_color_map({"a": YELLOW,
                                                "b": RED,
                                                "x": ORANGE})
        self.play(FadeIn(eqns2_s3))
        self.wait(3)

        eqns2_s4 = MathTex(r" x^2 = x +x + x +\cdots + x", substrings_to_isolate=["x"])
        eqns2_s4.next_to(eqns2_s3, DOWN)
        eqns2_s4.set_color_by_tex_to_color_map({"x": ORANGE})

        Bi = Brace(eqns2_s4[3:], DOWN)
        ti = Bi.get_tex(r"(", r"x", r"~ \mathrm{times})")
        ti[1].set_color(ORANGE)

        grp = VGroup(Bi,ti)

        self.play(FadeIn(eqns2_s4))
        self.play(FadeIn(grp))
        self.wait(6)

        self.play(FadeOut(eqns1_s2),
                  FadeOut(eqns2_s2),
                  FadeOut(eqns2_s3),
                  FadeOut(eqns2_s4),
                  FadeOut(Bi1),
                  FadeOut(ti1),
                  FadeOut(grp),
                  FadeOut(pg_title),
                  )

    def scene_5(self):
        eqns1_s3 = MathTex(r"\frac{d}{dx}x^n = n x^{n-1}", substrings_to_isolate=["x", "n"])
        eqns1_s3.set_color_by_tex_to_color_map({"x": ORANGE,
                                                "n": BLUE})
        eqns1_s3.shift(UP)
        self.play(FadeIn(eqns1_s3))
        self.wait(2)
        self.play(FadeOut(eqns1_s3))

    def scene_6(self):
        eqns1_s4 = MathTex(r"\frac{d}{dx}x^2 =", r"\frac{d}{dx}(x +x + x + \cdots + x)", substrings_to_isolate=["x"])
        eqns1_s4.set_color_by_tex_to_color_map({"x": ORANGE})
        eqns1_s4.shift(UP)

        Bi = Brace(eqns1_s4[8:-1], UP)
        ti = Bi.get_tex(r"(", r"x", r"~ \mathrm{times})")
        ti[1].set_color(ORANGE)

        grp = VGroup(eqns1_s4, Bi,ti)

        self.play(FadeIn(eqns1_s4))
        self.play(FadeIn(Bi,ti))
        self.play(ApplyMethod(grp.shift, UP))
        self.wait(2)

        eqns2_s4 = MathTex(r"{{2x= \frac{d}{dx}x + \frac{d}{dx}x + \frac{d}{dx}x + \cdots \quad (x}}~\mathrm{times})",
                           substrings_to_isolate=["x"])
        eqns2_s4.next_to(eqns1_s4, DOWN)
        eqns2_s4.set_color_by_tex_to_color_map({"x": ORANGE})
        self.play(FadeIn(eqns2_s4))
        self.wait(2)

        eqns3_s4 = MathTex(r"{{2x =1 + 1 + 1 + \cdots \quad (x~}} \mathrm{times})", substrings_to_isolate=["x"])
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

        self.play(
            FadeOut(eqns1_s4),
            FadeOut(Bi),
            FadeOut(ti),
            FadeOut(eqns2_s4),
            FadeOut(eqns3_s4),
            FadeOut(eqns4_s4),
        )

        #  t = ValueTracker(5)
        text_note = Text("Video resume in:").scale(0.8)
        t5 = MathTex("5").set_color(ORANGE)
        t5.next_to(text_note, DOWN)

        t4 = MathTex("4").set_color(ORANGE)
        t4.next_to(text_note, DOWN)

        t3 = MathTex("3").set_color(ORANGE)
        t3.next_to(text_note, DOWN)

        t2 = MathTex("2").set_color(ORANGE)
        t2.next_to(text_note, DOWN)

        t1 = MathTex("1").set_color(ORANGE)
        t1.next_to(text_note, DOWN)

        self.play(
            FadeIn(text_note, t5),
        )
        self.play(Transform(t5, t4))
        self.play(Transform(t5, t3))
        self.play(Transform(t5, t2))
        self.play(Transform(t5, t1))

        self.play(
            FadeOut(text_note),
            FadeOut(t5)
        )

    def scene_7(self):
        equation = MathTex(r"f(x)=x^2", font_size=30, substrings_to_isolate=["x"])
        equation.move_to(2.5*UP)
        equation.set_color_by_tex_to_color_map({"x": ORANGE})

        # Continous graph
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

        # Discrete graph
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
        self.play(Create(ax),
                  Create(labels),
                  Create(curve_1),
                  )
        self.play(
            Create(ax2),
            Create(labels2),
            Create(curve_2["vertex_dots"]),
        )
        self.play(Write(equation2))

        self.wait(2)

        self.play(
            FadeOut(equation),
            FadeOut(grp1),
            FadeOut(grp2),
            FadeOut(equation2),
        )

        """ Animate the tangent as derivative"""
        # Continous graph
        ax = Axes(
            x_range=[0, 4, 0.5],
            y_range=[0, 16, 1],
            axis_config={"include_tip": False,
                         "include_numbers": True}
        )
        labels = ax.get_axis_labels(x_label="x",
                                    y_label="f(x)")

        func = ax.plot(lambda x: x ** 2, x_range=[0, 4], color=BLUE_C)

        plt_grp = Group(ax, labels, func)
        plt_grp.scale(0.8)

        x = ValueTracker(2.0)
        dx = ValueTracker(1)

        secant = always_redraw(
            lambda: ax.get_secant_slope_group(
                x=x.get_value(),
                graph=func,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                #  dx_label="dx",
                dy_label="dy",
                secant_line_color=GREEN,
                secant_line_length=6,
            )
        )

        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(ax.c2p(x.get_value(), func.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(
                ax.c2p(
                    (x).get_value() + dx.get_value(),
                    func.underlying_function(x.get_value() + dx.get_value()),
                )
            )
        )
        secat_grp = VGroup(dot1, dot2, secant)

        dx_var = Variable(dx.get_value(), 'dx', num_decimal_places=3)
        dx_var.scale(0.7)
        dx_var.next_to(dot1, RIGHT)
        dx_var.shift(0.5*DOWN)
        dx_var.set_color(YELLOW)
        dx_var.add_updater(lambda v: v.tracker.set_value(dx.get_value()))

        v_line1 = always_redraw(lambda: ax.get_vertical_line(dot1.get_center()))
        v_line2 = always_redraw(lambda: ax.get_vertical_line(dot2.get_center()))

        self.play(Create(ax),
                  Create(labels),
                  Create(func),
                  )
        self.wait(2)
        self.play(
            Create(secat_grp),
            run_time=2
        )
        self.play(
            Create(v_line1),
            Create(v_line2),
        )
        self.add(dx_var)
        self.play(dx.animate.set_value(0.001),
                  dx_var.tracker.animate.set_value(0.001),
                  run_time=10)
        self.wait(2)
        self.play(
            FadeOut(secat_grp),
            FadeOut(dx_var),
            FadeOut(v_line1),
            FadeOut(v_line2),
        )


        """ Tranmsform into Discrete graph """
        x_pts = [x for x in arange(0, 4.5, 0.5)]
        y_pts = [x*x for x in arange(0, 4.5, 0.5)]
        curve_2 = ax.plot_line_graph(x_values=x_pts, y_values=y_pts, line_color=BLUE_C)

        x = ValueTracker(2.0)
        dx = ValueTracker(1)

        dot1 = Dot(ax.c2p(2, 4))
        dot2 = Dot(ax.c2p(3, 9))
        line = Line(start=dot1.get_center(), end=dot2.get_center()).set_color(GREEN)

        dot3 = Dot(ax.c2p(3, 4))
        h_line_discrete = Line(start=dot1.get_center(), end=dot3.get_center()).set_color(YELLOW)
        v_line_discrete = Line(start=dot2.get_center(), end=dot3.get_center()).set_color(ORANGE)

        Y_label = MathTex("dy").set_color(ORANGE)
        Y_label.scale(0.8)
        Y_label.next_to(v_line_discrete, 0.5*RIGHT)
        extra_lines_grp = VGroup(h_line_discrete, v_line_discrete, Y_label)

        v_line1 = always_redraw(lambda: ax.get_vertical_line(ax.c2p(2, 4)))
        v_line2 = always_redraw(lambda: ax.get_vertical_line(ax.c2p(3, 9)))

        dx_var = Variable(1, 'dx', num_decimal_places=3)
        dx_var.scale(0.7)
        dx_var.next_to(dot1, RIGHT)
        dx_var.shift(0.5*DOWN)
        dx_var.set_color(YELLOW)


        self.play(Transform(func, curve_2["vertex_dots"]))
        self.play(
            Create(line),
            run_time=2
        )
        self.play(
            Create(v_line1),
            Create(v_line2),
            Create(extra_lines_grp),
        )
        self.add(dx_var)
        self.wait(4)

        self.play(
            FadeOut(plt_grp),
            FadeOut(dx_var),
            FadeOut(line),
            FadeOut(v_line1),
            FadeOut(v_line2),
            FadeOut(extra_lines_grp),
        )


        """ Scene """
        pg_title = Text("Two explanations", font_size=25, color=TEAL)
        pg_title.shift(3*UP)
        pg_title.shift(5*LEFT)

        eq1 = MathTex(r"x^2 =x+x+\cdots+x + (x-\lfloor x \rfloor) \cdot x", substrings_to_isolate=["x"])
        eq1.set_color_by_tex_to_color_map({"x": ORANGE})
        eq1.move_to(2*UP)
        l1_txt = Text("(1)", font_size=15)
        l1_txt.next_to(eq1, 5*RIGHT)

        Bi = Brace(eq1[2:7], DOWN)
        ti = Bi.get_tex(r"\lfloor", r"x", r"\rfloor \mathrm{~times}")
        ti[1].set_color(ORANGE)
        grp = VGroup(eq1, Bi,ti, l1_txt)

        eq2 = MathTex(r"{d \over dx}(xf(x)) =x \cdot {d \over dx} f(x) +", r"1", r"\cdot f(x)", substrings_to_isolate=["x"])
        eq2.set_color_by_tex_to_color_map({"x": ORANGE})
        eq2.next_to(grp, 2*DOWN)
        l2_txt = Text("(2)", font_size=15)
        l2_txt.next_to(eq2, 3*RIGHT)
        grp2 = VGroup(eq2, l2_txt)

        frameBoxa = SurroundingRectangle(eq2[13:17], buff=0.8 * SMALL_BUFF)
        frameBoxa.set_stroke(BLUE, 3)
        boxtextea1 = Text("Didn't account for this part", font_size=15)
        boxtextea2 = Text("in the previous analysis", font_size=15)
        boxtextea1.next_to(eq2[13:17].get_center(), UP, buff=0.7)
        boxtextea2.next_to(boxtextea1.get_center(), 0.5*DOWN)
        grp_txt = VGroup(boxtextea1, boxtextea2)
        grp_txt.set_color(BLUE, 3)

        eq3 = MathTex(r"{d \over dx}(x \cdot x) & ={dx \over dx} \cdot x + x \cdot {dx \over dx} \\  &=2x", substrings_to_isolate=["x"])
        eq3.set_color_by_tex_to_color_map({"x": ORANGE})
        eq3.next_to(eq2, 2*DOWN)

        self.play(FadeIn(pg_title))
        self.play(FadeIn(grp))
        self.wait(2)
        self.play(FadeIn(grp2))
        self.wait(1)

        self.play(Create(frameBoxa))
        self.play(Write(grp_txt))

        self.wait(2)
        self.play(FadeIn(eq3))

        self.wait(2)

        self.play(
            FadeOut(pg_title),
            FadeOut(grp),
            FadeOut(grp2),
            FadeOut(frameBoxa),
            FadeOut(grp_txt),
            FadeOut(eq3),
        )

    def scene_thanks(self):
        last_text = Tex("Thanks!")
        self.play(Write(last_text))
        self.wait(2)
        self.play(FadeOut(last_text))

