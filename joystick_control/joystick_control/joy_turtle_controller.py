import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyTurtleController(Node):
    def __init__(self):
        super().__init__('joy_turtle_controller')
        self.subscription = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Velocidades base (normales) haciendo pruebas, si se incrementa, se traba en VB
        self.base_lin = 2.0
        self.base_ang = 2.0

    def joy_callback(self, msg):
        twist = Twist()
        
        # Multiplicador de velocidad por defecto
        speed_multiplier = 1.0
        
        # Verificamos si los botones R1 o L1 están presionados (valor = 1)
        # Nota: L1 suele ser msg.buttons[4] y R1 suele ser msg.buttons[5]
        if msg.buttons[5] == 1:     # R1 presionado -> Modo Turbo
            speed_multiplier = 2.0
        elif msg.buttons[4] == 1:   # L1 presionado -> Modo Lento (Precisión)
            speed_multiplier = 0.5
            
        # Calculamos la velocidad máxima actual aplicando el multiplicador
        current_max_lin = self.base_lin * speed_multiplier
        current_max_ang = self.base_ang * speed_multiplier

        # Mapeo de movimiento (Palanca izquierda)
        twist.linear.x = msg.axes[1] * current_max_lin
        twist.angular.z = msg.axes[0] * current_max_ang
        
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = JoyTurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
