import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SicaklikIzleyici(Node):

    def __init__(self):
        super().__init__('sicaklik_izleyici')
        
        self.declare_parameter('esik_degeri', 30.0)
        self.esik_degeri = self.get_parameter('esik_degeri').value

        self.subscription = self.create_subscription(
            Float32,
            'sicaklik',
            self.sicaklik_callback,
            10
        )

        self.get_logger().info('Sicaklik izleyici baslatildi.')

    def sicaklik_callback(self, msg):
        sicaklik = msg.data

        self.get_logger().info(
            f'Gelen sicaklik: {sicaklik:.2f} derece'
        )

        if sicaklik > self.esik_degeri:
            self.get_logger().warn(
                f'UYARI! Sicaklik 30 derecenin uzerinde: {sicaklik:.2f}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = SicaklikIzleyici()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
