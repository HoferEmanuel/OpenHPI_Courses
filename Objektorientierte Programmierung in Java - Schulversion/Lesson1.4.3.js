class Calculation {
	public static void main(String[] args) {
        int mainBattery = 7;
        int replacementBattery = 5;
        int runtime;
        String result;
        
        runtime = mainBattery + replacementBattery;
        result = ("Robin hat insgesamt eine Laufzeit von: " + runtime + " Stunden");
                
        System.out.println(result);
	}
}
