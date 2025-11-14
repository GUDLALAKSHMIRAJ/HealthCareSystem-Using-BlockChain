// SPDX-License-Identifier: MIT
pragma solidity >= 0.4.0 <= 0.9.0;

contract Report {
    string public hospital_details;
    string public patient_details;
    string public prescription;
       
    function setHospital(string memory hd) public {
        hospital_details = hd;    
    }
   
    function getHospital() public view returns (string memory) {
        return hospital_details;
    }

    function setPatient(string memory pd) public {
        patient_details = pd; 
    }
   
    function getPatient() public view returns (string memory) {
        return patient_details;
    }

    function setPrescription(string memory p) public {
        prescription = p; 
    }
   
    function getPrescription() public view returns (string memory) {
        return prescription;
    }

    constructor() {
        hospital_details="";
        prescription = "";
        patient_details="";
    }
}
