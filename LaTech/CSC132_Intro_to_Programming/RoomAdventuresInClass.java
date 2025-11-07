import java.util.Scanner;

public class RoomAdventuresInClass {
    // Class variables
    private static Room currentRoom;
    private static String[] inventory = {null, null, null, null, null};
    private static String status;

    // constants
    final private static String DEFAULT_STATUS = "Sorry, I do not understand. Valid input should be like: [verb] [noun]. Valid verbs include 'go', 'look', and 'take'.";

    // Main function
    public static void main(String[] args){
        setupGame();



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
            
                    
            
        }




        // setup game
        private static void setupGame(){

            Room room1 = new Room("Room 1");
            Room room2 = new Room("Room 2");

            // Room 1
            String[] room1ExitDirections = {"east", "south"}; // declaring an array
            Room[] room1ExitDestinations = {room2};
            String[] room1Items = {"chair", "desk"};
            String[] room1ItemDescriptions = {
                "It is a chair, there is a nail on it.", 
                "It's a desk, there is an apple on it."
            };
            String[] room1Grabbables = {"nail", "apple"};

            room1.setExitDirections(room1ExitDirections);
            room1.setExitDestinations(room1ExitDestinations);
            room1.setItems(room1Items);
            room1.setItemDescriptions(room1ItemDescriptions);
            room1.setGrabbables(room1Grabbables);

            // Room 2
            String[] room2ExitDirections = {"west"}; // declaring an array
            Room[] room2ExitDestinations = {room1};
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


}


Class Room{
    private String name;
    private String[] exitDirections; // north, south, east, west
    private Room[] exitDestinations;
    private String[] items;
    private String[] itemDescriptions;
    private String[] grabbables;

    // constructors - function has same name as class
    public Room(String name){
        this.name = name; // use this to refer to the instance when it is unclear
    }

    // Getters and setters for Exit Directions
    public void setExitDirections(String[] exitDirections){
        this.exitDirections = exitDirections;
    }

    public String[] getExitDirections(){
        return exitDirections;
    }

    // Getters and setters for Exit Destinations
    public void setExitDestinations(Room[] exitDestinations){
        this.exitDestinations = exitDestinations;
    }

    public Room[] getExitDestinations(){
        return exitDestinations;
    }

    public void setItems(String[] items){
        this.items = items;
    }

    // Getters and setters for Items
    public String[] getItems(){
        return items;
    }

    public void setItemDescriptions(String[] itemDescriptions){
        this.itemDescriptions = itemDescriptions;
    }

    // Getters and setters for Item Descriptions
    public String[] getItemDescriptions(){
        return itemDescriptions;
    }

    // Getters and setters for Grabbables
    public void setGrabbables(String[] grabbables){
        this.grabbables = grabbables;
    }   

    public String[] getGrabbables(){
        return grabbables;
    }

    public String toString(){
        String result = "\n";
        result += "Location: " + name;
        
        result += "\nYou see: ";
        for(int i=0; i<items.length; i++){
            result += items[i] + " ";
        }

        result += "\nExits: ";
        // for each loop
        for (String direction : exitDirections){
            result += direction + " ";
        }

        return result += "\n";
    }
}