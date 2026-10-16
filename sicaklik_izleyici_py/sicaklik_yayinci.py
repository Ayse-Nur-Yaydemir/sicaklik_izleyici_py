import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class SicaklikYayinci(Node):

    def __init__(self):
        super().__init__('sicaklik_yayinci')

        self.publisher_ = self.create_publisher(
            Float32,
            'sicaklik',
            10
        )

        self.timer = self.create_timer(1.0, self.sicaklik_yayinla)

        self.get_logger().info('Sicaklik yayinci baslatildi.')

    def sicaklik_yayinla(self):
        mesaj = Float32()
        mesaj.data = float(random.uniform(20.0, 40.0))

        self.publisher_.publish(mesaj)

        self.get_logger().info(
            f'Yayinlanan sicaklik: {mesaj.data:.2f} derece'
        )


def main(args=None):
    rclpy.init(args=args)

    node = SicaklikYayinci()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
