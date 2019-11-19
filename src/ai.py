if __name__ == '__main__':
    monitor = Client_monitor('localhost', 4001)
    control = Client_control('localhost', 4002)

    while True:
        # return numpy matrix
        monitor.getImg();

        '''
            Обработка изображения
        '''

        '''
            Принятие решения
        '''

        # return True or False
        control.mouseClick(x=100, y=100)

