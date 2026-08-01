from manim import *

BG = "#1C1C1C"
PRIMARY = "#58C4DD"
SECONDARY = "#83C167"
ACCENT = "#FFFF00"
VERIFY = "#FF6B6B"
STRUCTURE = "#A0A0A0"
MONO = "DejaVu Sans Mono"


def clean_exit(scene):
    if scene.mobjects:
        scene.play(FadeOut(Group(*scene.mobjects)), run_time=0.6)
        scene.wait(0.3)


class Scene1_Question(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("SOLVING AN INTEGRAL", font=MONO, font_size=34,
                     weight=BOLD, color=PRIMARY).to_edge(UP, buff=0.65)
        integral = MathTex(r"\int x^2\,dx", font_size=86, color=WHITE)
        prompt = Text("Find a function whose derivative is x²",
                      font=MONO, font_size=25, color=STRUCTURE).next_to(integral, DOWN, buff=0.75)
        prompt.set_opacity(0.75)

        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=1.2)
        self.wait(0.7)
        self.play(GrowFromCenter(integral), run_time=1.7)
        self.wait(1.3)
        self.play(FadeIn(prompt, shift=UP * 0.2), run_time=1.0)
        self.wait(2.0)
        clean_exit(self)


class Scene2_Geometry(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = Text("INTEGRATION ACCUMULATES AREA", font=MONO, font_size=30,
                       weight=BOLD, color=SECONDARY).to_edge(UP, buff=0.55)
        axes = Axes(
            x_range=[0, 3.2, 1], y_range=[0, 9.5, 2],
            x_length=6.0, y_length=4.7,
            axis_config={"color": STRUCTURE, "stroke_opacity": 0.35,
                         "include_tip": False},
        ).shift(LEFT * 3.15 + DOWN * 0.35)
        x_label = axes.get_x_axis_label(MathTex("x", color=STRUCTURE), edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label(MathTex("y", color=STRUCTURE), edge=UP, direction=LEFT)
        graph = axes.plot(lambda x: x**2, x_range=[0, 3.05], color=PRIMARY, stroke_width=5)
        graph_label = MathTex(r"y=x^2", color=PRIMARY, font_size=36).move_to(axes.c2p(2.45, 7.3))
        area = axes.get_area(graph, x_range=[0, 2.5], color=SECONDARY, opacity=0.55)
        a_marker = DashedLine(axes.c2p(2.5, 0), axes.c2p(2.5, 6.25),
                              color=ACCENT, stroke_opacity=0.8)
        a_label = MathTex("a", color=ACCENT, font_size=34).next_to(axes.c2p(2.5, 0), DOWN, buff=0.18)

        idea = VGroup(
            Text("Area up to a", font=MONO, font_size=25, color=SECONDARY),
            MathTex(r"A(a)=\int_0^a x^2\,dx", font_size=40),
            MathTex(r"A(a)=\frac{a^3}{3}", font_size=48, color=SECONDARY),
        ).arrange(DOWN, buff=0.55).move_to(RIGHT * 3.55 + DOWN * 0.15)

        self.play(FadeIn(heading), run_time=1.0)
        self.wait(0.5)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=1.2)
        self.wait(0.5)
        self.play(Create(graph), FadeIn(graph_label), run_time=2.0)
        self.wait(0.8)
        self.play(FadeIn(area), Create(a_marker), FadeIn(a_label), run_time=1.7)
        self.wait(1.3)
        self.play(FadeIn(idea[0], shift=UP * 0.2), Write(idea[1]), run_time=1.3)
        self.wait(1.0)
        self.play(TransformFromCopy(idea[1], idea[2]), run_time=1.5)
        self.wait(2.0)
        clean_exit(self)


class Scene3_PowerRule(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = Text("USE THE POWER RULE", font=MONO, font_size=32,
                       weight=BOLD, color=ACCENT).to_edge(UP, buff=0.6)
        rule = MathTex(r"\int x^n\,dx=\frac{x^{n+1}}{n+1}+C",
                       font_size=53, color=WHITE).shift(UP * 1.25)
        rule.set_color_by_tex("n+1", ACCENT)

        start = MathTex(r"\int x^2\,dx", font_size=58, color=PRIMARY).shift(LEFT * 4.3 + DOWN * 0.7)
        arrow1 = Arrow(LEFT * 2.7 + DOWN * 0.7, LEFT * 0.9 + DOWN * 0.7,
                       buff=0.1, color=ACCENT)
        add_one = VGroup(
            Text("add 1", font=MONO, font_size=20, color=ACCENT),
            MathTex(r"x^{2+1}", font_size=52, color=WHITE),
        ).arrange(DOWN, buff=0.22).move_to(DOWN * 0.7)
        arrow2 = Arrow(RIGHT * 1.0 + DOWN * 0.7, RIGHT * 2.6 + DOWN * 0.7,
                       buff=0.1, color=ACCENT)
        result = MathTex(r"\frac{x^3}{3}+C", font_size=62, color=SECONDARY).shift(RIGHT * 4.25 + DOWN * 0.7)
        divide = Text("divide by 3", font=MONO, font_size=20, color=ACCENT).next_to(result, UP, buff=0.35)

        self.play(FadeIn(heading, shift=DOWN * 0.2), run_time=1.0)
        self.wait(0.6)
        self.play(Write(rule), run_time=1.7)
        self.wait(1.5)
        self.play(FadeIn(start, shift=RIGHT * 0.2), run_time=0.9)
        self.play(GrowArrow(arrow1), FadeIn(add_one), run_time=1.1)
        self.wait(0.8)
        self.play(GrowArrow(arrow2), FadeIn(divide), TransformFromCopy(add_one[1], result), run_time=1.4)
        self.wait(2.3)
        clean_exit(self)


class Scene4_Verify(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = Text("CHECK BY DIFFERENTIATING", font=MONO, font_size=31,
                       weight=BOLD, color=VERIFY).to_edge(UP, buff=0.6)
        check1 = MathTex(r"\frac{d}{dx}\left(\frac{x^3}{3}+C\right)",
                         font_size=52).shift(UP * 1.25)
        check2 = MathTex(r"=\frac{1}{3}\cdot 3x^2+0", font_size=52).shift(DOWN * 0.15)
        check3 = MathTex(r"=x^2", font_size=62, color=PRIMARY).shift(DOWN * 1.55)
        box = SurroundingRectangle(check3, color=ACCENT, buff=0.25, stroke_width=4)
        final = MathTex(r"\boxed{\int x^2\,dx=\frac{x^3}{3}+C}",
                        font_size=59, color=SECONDARY)

        self.play(FadeIn(heading), run_time=1.0)
        self.wait(0.6)
        self.play(Write(check1), run_time=1.5)
        self.wait(1.0)
        self.play(TransformFromCopy(check1, check2), run_time=1.4)
        self.wait(0.9)
        self.play(TransformFromCopy(check2, check3), Create(box), run_time=1.5)
        self.wait(2.2)
        self.play(FadeOut(VGroup(check1, check2, check3, box, heading)), run_time=0.7)
        self.play(GrowFromCenter(final), run_time=1.8)
        self.wait(3.0)
        clean_exit(self)
