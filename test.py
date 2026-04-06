import hashlib
from sha256 import sha256

def test_sha256():
    print("--- Starting SHA-256 Test Suite ---\n")
    
    test_cases = [
        "",                                    
        "abc",                                
        "Mallhar",                             
        "Hello, World!",                       
        "a" * 55,                            
        "a" * 56,                              
        (                                     
            
            "My soldiers, rage! My soldiers, scream! My soldiers, fight! These are "
            "the brave fallen! The anguished fallen! Their lives have meaning because "
            "we the living refuse to forget them! And as we ride to certain death, "
            "we trust our successors to do the same for us!"
        
        )
    ]

    passed = 0
    failed = 0

    for i, message in enumerate(test_cases):
        print(f"Test {i+1}: {message}")
        
        official_hash = hashlib.sha256(message.encode('utf-8')).hexdigest()
        
        your_hash = sha256(message)
        
        if official_hash == your_hash:
            print("  ✅ PASS")
            passed += 1
        else:
            print("  ❌ FAIL")
            print(f"     Expected: {official_hash}")
            print(f"     Got:      {your_hash}")
            failed += 1
            
    print(f"Total Tests: {len(test_cases)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    

if __name__ == "__main__":
    test_sha256()