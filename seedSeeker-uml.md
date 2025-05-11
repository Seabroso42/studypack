::: mermaid
classDiagram
  direction LR
    class Keeper {
        +String name
        +String email
        +String password
        +int level
        +int experience
        +int levelupBar
        +Garden garden
        +List~Achievement~ achievements
        +addExperience(points: int) void
    }

    class Garden {
        -Keeper owner
        +String name
        +List~Plant~ plants
        +integer numberofplants
        +Plant bestPlant
        +addPlant(plant: Plant) void
        +removePlant()
    }

    class Plant {
        +String image_url
        +String name
        +Species species
        +HealthEnum HealthStatus
        +boolean isAlive
        +WaterEnum WaterLevel
        +int healthBar
        +List~Task~ tasks
        +warn(String message)
        +addTask(task: Task) void
        +triggerWatering(waterLevel: WaterLevel) void
    }


    class TelemetryParameter {
      +String parameterName
      +float defaultValue
      +float criticalValue

    }

    class Species {
        +String name
        +Strinf scientificName
        +List~TelemetryParameter~ monitoringParameters
        +Soil soil
    }

    class Task {
        +String name
        +TaskTypes type
        +double timer
        +String description
        +int experiencePoints
        +Plant plant
        +complete() void
        +warn() void

    }

    class Achievement {
        +String title
        +String description
    }

    class Soil {
        +String type
        +int pHLevel
        +int moistureLevel
    }

    class Notification{
      +Keeper destiny
      +String text
      +NotiTypes type
      +String icon_url
    }

    class enums{
      +enum plantImages
      +enum WaterLevels
      +enum SunExposure
      +enum HealthStatus
      +enum AchievementType
      +enum AchievementRarity
      +enum SoilType
      +enum TaskRecurrency
      +enum TaskType
      +enum UserRanking
    }

    Keeper "1" -- "1" Garden : manages
    Garden "1" -- "*" Plant : contains
    Plant "1" -- "1" Species : has
    Plant "1" -- "*" Task : has
    Task "1" -- "1" Plant : assigned to
    Species "1" -- "1" Soil : requires
    Species "1" -- "*" TelemetryParameter : requires
    Keeper "1" -- "*" Achievement : earns
    Keeper "1" -- "*" Notification : receives

:::