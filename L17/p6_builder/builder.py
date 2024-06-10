from abc import ABC, abstractmethod


class EnvironmentBuilder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def deploy_os_image(self):
        pass

    @abstractmethod
    def create_virtual_env(self):
        pass

    @abstractmethod
    def install_libs(self):
        pass

    @abstractmethod
    def install_app(self):
        pass

    def get_environment(self):
        pass


class TestingEnvBuilder(EnvironmentBuilder):

    def __init__(self):
        self.environment = Environment()
        self.reset()

    def deploy_os_image(self):
        stage = "Deploying os image on test env..."
        self.environment.update_performed_stages(stage)
        print(stage)

    def create_virtual_env(self):
        stage = "Creating virtual env on test env..."
        self.environment.update_performed_stages(stage)
        print(stage)

    def install_libs(self):
        stage = "Installing libs.md on test env..."
        self.environment.update_performed_stages(stage)
        print(stage)

    def install_app(self):
        stage = "Installing app on test env..."
        self.environment.update_performed_stages(stage)
        print(stage)

    def reset(self):
        print("Clearing test env...")
        self.environment.clear()

    def get_environment(self):
        import copy
        environment = copy.deepcopy(self.environment)
        self.reset()
        return environment


class Environment:

    def __init__(self):
        self.performed_stages = []

    def update_performed_stages(self, stage):
        self.performed_stages.append(stage)

    def clear(self):
        self.performed_stages.clear()

    def __str__(self):
        NEWLINE_SYMBOL = '\n'
        return f"{NEWLINE_SYMBOL.join(self.performed_stages)}"


class EnvDirector:

    def create_full_env(self, builder: EnvironmentBuilder):
        builder.deploy_os_image()
        builder.create_virtual_env()
        builder.install_libs()
        builder.install_app()
        return builder.get_environment()

    def create_env_without_app(self, builder: EnvironmentBuilder):
        builder.deploy_os_image()
        builder.create_virtual_env()
        builder.install_libs()
        return builder.get_environment()


if __name__ == '__main__':
    test_env_builder = TestingEnvBuilder()

    env_director = EnvDirector()
    full_environment = env_director.create_full_env(test_env_builder)
    print()
    print(full_environment)
    print()
    environment_without_app = env_director.create_env_without_app(test_env_builder)
    print()
    print(environment_without_app)
