from gym.envs.registration import register

register(
    id='voronoi-v0',
    entry_point='gym_voronoi.envs:VoronoiEnv',
)