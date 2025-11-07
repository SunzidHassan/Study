import java.util.Scanner;

public class RoomAdventure{

    // class variables
    private static Room currentRoom;
    private static String[] inventory = {null, null, null, null, null};
    private static String status;

    // constants
    final private static String DEFAULT_STATUS = "Sorry, I do not understand. Try [verb] [noun]. Valid verbs include 'go', 'look', and 'take'.";

    // the window into any class when you "run" the program.
    // acts like the part of a python program that isn't inside any sort of function ("main")
    public static void main(String[] args){
         
        setupGame();

        // while loops
        while (true){
            // outputting
            System.out.println(currentRoom.toString());
            System.out.print("Inventory: ");

            // for loops
            for (int i = 0; i < inventory.length; i++){
                System.out.print(inventory[i] + " ");
            }

            System.out.println("\nWhat would you like to do? ");
        

            // taking input
            Scanner s = new Scanner(System.in);
            String input = s.nextLine();
            
            String[] words = input.split(" ");

            if (words.length != 2){
                status = DEFAULT_STATUS;
            }

            String verb = words[0];
            String noun = words[1];

            switch (verb){
                case "go":
                    handleGo(noun);
                    break;
                case "look":
                    handleLook(noun);
                    break;
                case "take":
                    handleTake(noun);
                    break;
                default: status = DEFAULT_STATUS;
            }
            
            System.out.println(status);
            
                    
            
        }

    }

    private static void handleGo(String noun){
        String[] exitDirections = currentRoom.getExitDirections();
        Room[] exitDestinations = currentRoom.getExitDestinations();
        status = "I don't see that room.";
        for (int i = 0; i < exitDirections.length; i++){
            if (noun.equals(exitDirections[i])){
                currentRoom = exitDestinations[i];
                status = "Changed Room";
            }
        }
    }

    private static void handleLook(String noun){
        String[] items = currentRoom.getItems();
        String[] itemDescriptions = currentRoom.getItemDescriptions();
        status = "I don't see that item.";
        for (int i = 0; i < items.length; i++){
            if (noun.equals(items[i])){
                status = itemDescriptions[i];
            }
        }
    }

    private static void handleTake(String noun){
        String[] grabbables = currentRoom.getGrabbables();
        status = "I can't grab that.";
        for (int i = 0; i < grabbables.length; i++){
            if (noun.equals(grabbables[i])){
                for (int j = 0; j < inventory.length; j++){
                    if (inventory[j] == null){
                        inventory[j] = noun;
                        status = "Added it to the inventory";
                        break;
                    }
                }
            }
        }
    }

    private static void setupGame(){
        Room room1 = new Room("Room 1"); // instantiation of an object
        Room room2 = new Room("Room 2");

        // Room 1
        String[] room1ExitDirections = {"east", "south"}; // declaring an array
        Room[]   room1ExitDestinations = {room2};

        String[] room1Items = {"chair", "desk"};
        String[] room1ItemDescriptions = {
            "It is a chair", 
            "It's a desk, there is a key on it."
        };

        String[] room1Grabbables = {"key"};

        room1.setExitDirections(room1ExitDirections);
        room1.setExitDestinations(room1ExitDestinations);
        room1.setItems(room1Items);
        room1.setItemDescriptions(room1ItemDescriptions);
        room1.setGrabbables(room1Grabbables);

        // Room 2
        String[] room2ExitDirections = {"west"};
        Room[]   room2ExitDestinations = {room1};
        String[] room2Items = {"fireplace", "rug"};
        String[] room2ItemDescriptions = {
            "Its on fire", 
            "There is a lump of coal on the rug."
        };
        String[] room2Grabbables = {"coal"};
        room2.setExitDirections(room2ExitDirections);
        room2.setExitDestinations(room2ExitDestinations);
        room2.setItems(room2Items);
        room2.setItemDescriptions(room2ItemDescriptions);
        room2.setGrabbables(room2Grabbables);

        currentRoom = room1;
    }
}

// declaring a class
class Room{

    // instance variables (class variables will have the word static)
    // private means only available to being referenced inside this class
    // public can be referenced outside of this class
    // must declare data type
    private String name;
    private String[] exitDirections;    // north, south, east, west
    private Room[] exitDestinations;
    private String[] items;
    private String[] itemDescriptions;
    private String[] grabbables;

    // constructors - function has same name as class
    public Room(String name){
        this.name = name; // use this to refer to the instance when it is unclear
    }

    // other methods
    public void setExitDirections(String[] exitDirections){
        this.exitDirections = exitDirections;
    }
    

    public String[] getExitDirections(){
        return exitDirections;
    }
    
    public void setExitDestinations(Room[] exitDestinations){
        this.exitDestinations = exitDestinations;
    }

    public Room[] getExitDestinations(){
        return exitDestinations;
    }

    public void setItems(String[] items){
        this.items = items;
    }

    public String[] getItems(){
        return items;
    }
    
    public void setItemDescriptions(String[] itemDescriptions){
        this.itemDescriptions = itemDescriptions;
    }

    public String[] getItemDescriptions(){
        return itemDescriptions;
    }


    public String[] getGrabbables(){
        return grabbables;
    }

    public void setGrabbables(String[] grabbables){
        this.grabbables = grabbables;
    }



    public String toString(){
        String result = "\n";
        result += "Location: " + name;

        result += "\nYou See: ";
        // for loop
        for (int i = 0; i < items.length; i++){
            result += items[i] + " ";
        }

        result += "\nExits: ";
        // for each loop
        for (String direction : exitDirections){
            result += direction + " ";
        }

        return result + "\n";
    }
}