Title: Python 设计模式(A)
Date: 2017-03-28 10:20
Modified: 2017-03-28 10:20
Category: Python
Tags: Python
Slug: D1
Authors: nJcx
Summary: Python 设计模式(A)
Status: draft
####介绍
这里列举了三种最基本的设计模式，一共有23种，当然，对于Python可能没有23种：

- 创建模式，提供实例化的方法，为适合的状况提供相应的对象创建方法。
- 结构化模式，通常用来处理实体之间的关系，使得这些实体能够更好地协同工作。
- 行为模式，用于在不同的实体建进行通信，为实体之间的通信提供更容易，更灵活的通信方法。


创建型 ：1. Factory Method（工厂方法）2. Abstract Factory（抽象工厂）3. Builder（建造者）4. Prototype（原型）5. Singleton（单例）

结构型 ： 6. Adapter Class/Object（适配器）7. Bridge（桥接）8. Composite（组合）9. Decorator（装饰）10. Facade（外观）11. Flyweight（享元）12. Proxy（代理）

行为型 ： 13. Interpreter（解释器）14. Template Method（模板方法）15. Chain of Responsibility（责任链）16. Command（命令）17. Iterator（迭代器）18. Mediator（中介者）
19. Memento（备忘录）20. Observer（观察者）21. State（状态）22. Strategy（策略）23. Visitor（访问者）

####工厂模式
目的：定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类。

适用：
当一个类不知道它所必须创建的对象的类的时候。
当一个类希望由它的子类来指定它所创建的对象的时候。
当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。





