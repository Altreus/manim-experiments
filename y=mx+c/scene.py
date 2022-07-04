from manim import *
from pprint import pprint

class LineOnGraph(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            tips=False,
            axis_config={"include_numbers": True},
        )

        m = -0.87
        c = 3
        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: m * x + c, x_range=[-10, 10])

        sample_point_a = ax.coords_to_point( 6, 4 )
        sample_point_b = ax.coords_to_point( -3, -4 )
        sample_point_c = ax.coords_to_point( -6, -1 )
        xform_point_a  = ax.coords_to_point( m * 6 + c, (4 - c) / m )
        xform_point_b  = ax.coords_to_point( m * -3 + c, (-4 - c) / m )
        xform_point_c  = ax.coords_to_point( m * -6 + c, (-1 - c) / m )

        line_sa_sb = Line(sample_point_a, sample_point_b, color=GREEN)
        line_sa_sc = Line(sample_point_a, sample_point_c, color=BLUE)
        line_xa_xb = Line(xform_point_a, xform_point_b, color=RED)
        line_xa_xc = Line(xform_point_a, xform_point_c, color=YELLOW)

        sample_dot_a = Dot(sample_point_a, color=GREEN)
        sample_dot_a2 = Dot(sample_point_a, color=BLUE)
        sample_dot_b = Dot(sample_point_b, color=GREEN)
        sample_dot_c = Dot(sample_point_c, color=BLUE)
        xform_dot_a  = Dot(xform_point_a, color=RED)
        xform_dot_a2 = Dot(xform_point_a, color=YELLOW)
        xform_dot_b  = Dot(xform_point_b, color=RED)
        xform_dot_c  = Dot(xform_point_c, color=YELLOW)

        vector_a     = Vector( [
                xform_dot_a.get_x() - sample_dot_a.get_x(),
                xform_dot_a.get_y() - sample_dot_a.get_y()
                ],
                color=GREY
            ).shift(sample_point_a).save_state()

        vector_b     = Vector( [
                xform_dot_b.get_x() - sample_dot_b.get_x(),
                xform_dot_b.get_y() - sample_dot_b.get_y()
                ],
                color=GREY
            ).shift(sample_point_b)

        vector_c     = Vector( [
                xform_dot_c.get_x() - sample_dot_c.get_x(),
                xform_dot_c.get_y() - sample_dot_c.get_y()
                ],
                color=GREY
            ).shift(sample_point_c)

        self.add(
                ax, graph,
                sample_dot_a,
                xform_dot_a,
                vector_a
                )

        self.play(
                Transform(sample_dot_a, sample_dot_b),
                Transform(xform_dot_a, xform_dot_b),
                Transform(vector_a, vector_b),
                Create(line_sa_sb),
                Create(line_xa_xb)
                )

        self.wait(1)

        vector_a.restore()
        self.add(
            sample_dot_a2,
            xform_dot_a2
            )

        self.play(
                Transform(sample_dot_a2, sample_dot_c),
                Transform(xform_dot_a2, xform_dot_c),
                Transform(vector_a, vector_c),
                Create(line_sa_sc),
                Create(line_xa_xc)
                )

        self.wait(1)
