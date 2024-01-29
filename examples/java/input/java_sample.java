    private void setNodekeyInJsonResponse(String service) throws Exception { 
        /**
         * This method sets the NODEKEY value in a JSON response file for a specified service.
         *
         * @param service The name of the service for which the JSON response file is being updated.
         * @throws Exception If there is an error while updating the JSON response file.
         */
        String filename = this.baseDirectory + service + ".json"; 
        Scanner s = new Scanner(new File(filename)); 
        PrintWriter fw = new PrintWriter(new File(filename + ".new")); 
        
        while (s.hasNextLine()) { 
            fw.println(s.nextLine().replaceAll("NODEKEY", this.key)); 
        } 
        
        s.close(); 
        fw.close(); 
        
        (new File(filename + ".new")).renameTo(new File(filename)); 
    }