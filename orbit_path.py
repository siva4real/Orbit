from manim import *
import numpy as np
'''
hours it takes to rotate around the sun 
    earth : 8,765.81277
    mars : 16,687.270

'''

class SolarSystem(Scene):
    def construct(self) :

        sun_core = Dot(color=YELLOW, radius=0.2)
        glow1 = Dot(color=YELLOW, radius=0.3, fill_opacity=0.3)
        glow2 = Dot(color=YELLOW, radius=0.4, fill_opacity=0.2)
        glow3 = Dot(color=YELLOW, radius=0.5, fill_opacity=0.1)
        sun = VGroup(glow3, glow2, glow1, sun_core)
        
        earth_orbit = ParametricFunction(
            lambda t: np.array([
                1.8 * np.cos(t),
                1.5 * np.sin(t),
                0
            ]),
            t_range=[0, TAU],
            color=BLUE_D,

        )
        
        tilt_angle = 20 * DEGREES
        mars_orbit = ParametricFunction(
            lambda t: np.array([
                3 * np.cos(t) * np.cos(tilt_angle) - 5 * np.sin(t) * np.sin(tilt_angle),
                3 * np.cos(t) * np.sin(tilt_angle) + 2 * np.sin(t) * np.cos(tilt_angle),
                0
            ]),
            t_range=[0, TAU],
            color=RED_D,
        )
        
        earth = Dot(color=BLUE, radius=0.15)
        mars = Dot(color=RED, radius=0.12)

        earth_period = 5.31659
        mars_period = 10 

        earth_to_sun_line = Line(earth.get_center(), ORIGIN, color=WHITE, stroke_width=1)
        earth_to_mars_line = Line(earth.get_center(), mars.get_center(), color=WHITE, stroke_width=1)

        angle_label = DecimalNumber(0, num_decimal_places=1)
        angle_label.scale(0.6)

        def update_angle_label(mob):
            # Get vectors for Earth-Sun and Earth-Mars
            v1 = earth_to_sun_line.get_vector()
            v2 = earth_to_mars_line.get_vector()
            
            # Calculate angle between vectors in degrees
            angle = angle_between_vectors(v1, v2) * 180 / PI
            
            # Update label value and position
            mob.set_value(angle)
            
            # Position label near the arc
            mob.move_to(DOWN * 0.35 + earth.get_center())
            return mob
        
        earth_to_sun_line.add_updater(
            lambda m: m.put_start_and_end_on(earth.get_center(), ORIGIN)
        )
        earth_to_mars_line.add_updater(
            lambda m: m.put_start_and_end_on(earth.get_center(), mars.get_center())
        )

        def get_orbit_position(t, a, b, period):
            # Implementation of Kepler's second law
            # Using true anomaly to ensure equal areas in equal times
            theta = 2 * PI * t / period
            r = (a * b) / np.sqrt((b * np.cos(theta))**2 + (a * np.sin(theta))**2)
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            return np.array([x, y, 0])
        
        earth.add_updater(
            lambda m, dt: m.move_to(
                get_orbit_position(
                    self.renderer.time,
                    earth_orbit.width/2,
                    earth_orbit.height/2,
                    earth_period
                )
            )
        )
        
        mars.add_updater(
            lambda m, dt: m.move_to(
                get_orbit_position(
                    self.renderer.time,
                    mars_orbit.width/2,
                    mars_orbit.height/2,
                    mars_period
                )
            )
        )

        earth_to_sun_line.add_updater(
            lambda m: m.put_start_and_end_on(earth.get_center(), ORIGIN)
        )
        earth_to_mars_line.add_updater(
            lambda m: m.put_start_and_end_on(earth.get_center(), mars.get_center())
        )

        angle_label.add_updater(update_angle_label)

        self.add(sun, earth_orbit, mars_orbit, 
                earth, mars, earth_to_sun_line, earth_to_mars_line,  angle_label)
        self.wait(16)  