import backend.models.action_model as actions
import backend.utils.attack_shapes as shapes
from backend.models import obstacle

cards = [
    actions.ActionCard(
        attack_name="Shockwave",
        actions=[
            actions.AreaAttackFromSelf(shape=shapes.circle(1), strength=3),
            actions.PushAllEnemies(1, 3),
        ],
        movement=1,
        jump=False,
    ),
    actions.ActionCard(
        attack_name="Ring of Fire",
        actions=[
            actions.AreaAttackFromSelf(
                shape=shapes.circle(2), element_type=obstacle.Fire, strength=2
            ),
        ],
        movement=1,
        jump=False,
    ),
    actions.ActionCard(
        attack_name="Explosive Blast",
        actions=[
            actions.AreaAttackFromSelf(shape=shapes.circle(2), strength=2),
            actions.WeakenEnemy(2, 2),
            actions.PushAllEnemies(2, 2),
        ],
        movement=1,
        jump=False,
    ),
    actions.ActionCard(
        attack_name="Storm of Blades",
        actions=[
            actions.AreaAttackFromSelf(shape=shapes.circle(1), strength=3),
            actions.AreaAttackFromSelf(shape=shapes.circle(2), strength=1),
        ],
        movement=2,
        jump=False,
    ),
    actions.ActionCard(
        attack_name="Earthquake",
        actions=[
            actions.AreaAttackFromSelf(shape=shapes.circle(2), strength=4),
            actions.MakeObstableArea(obstacle_type=obstacle.Rock, shape=shapes.arc(3)),
        ],
        movement=1,
        jump=True,
    ),
    actions.ActionCard(
        attack_name="Flame Wall",
        actions=[
            actions.AreaAttackFromSelf(
                shape=shapes.line(3), element_type=obstacle.Fire, strength=3
            ),
        ],
        movement=1,
        jump=False,
    ),
    actions.ActionCard(
        attack_name="Thunder Burst",
        actions=[
            actions.AreaAttackFromSelf(shape=shapes.circle(2), strength=4),
            actions.PushAllEnemies(1, 2),
        ],
        movement=1,
        jump=False,
    ),
]

health = 4
