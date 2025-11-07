class QuickStart {
    public static void main (String[] args) {
        String name = "Sunzid";
        String exclaim = addExclamationPoint(name);
        System.out.println(exclaim);
    }

    public static String addExclamationPoint(String s){
        return s + "!";
    }
}