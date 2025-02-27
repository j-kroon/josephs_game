// Create locations
CREATE (l1:Location {id: "location_1", name: "Haunted Forest", description: "A dark, eerie forest filled with twisted trees and strange noises."})
CREATE (l2:Location {id: "location_2", name: "Dark Cave", description: "A damp, dark cave with the sound of dripping water echoing through it."})

// Create items and relationships to locations
CREATE (i1:Item {id: "item_1", name: "Ancient Sword", description: "A rusted sword with mysterious engravings."})
CREATE (i2:Item {id: "item_2", name: "Magic Lantern", description: "A lantern that emits an eerie blue light."})
CREATE (i1)-[:LOCATED_IN]->(l1)
CREATE (i2)-[:LOCATED_IN]->(l1)

// Create interactions for items
CREATE (i1)-[:HAS_INTERACTION {action: "pick up", result: "You pick up the ancient sword, feeling its weight in your hand."}]->(i1)
CREATE (i1)-[:HAS_INTERACTION {action: "examine", result: "The sword is old and worn, but the engravings seem to glow faintly."}]->(i1)
CREATE (i2)-[:HAS_INTERACTION {action: "pick up", result: "You pick up the magic lantern, and it illuminates the surroundings."}]->(i2)
CREATE (i2)-[:HAS_INTERACTION {action: "use", result: "You use the lantern, revealing hidden paths in the forest."}]->(i2)

// Create exits and relationships to locations
CREATE (l1)-[:HAS_EXIT {direction: "north", leads_to: "location_2", description: "A narrow path leading deeper into the forest."}]->(l2)
CREATE (l1)-[:HAS_EXIT {direction: "east", leads_to: "location_3", description: "A faint trail leading to an abandoned cabin."}]->(l3)
CREATE (l2)-[:HAS_EXIT {direction: "south", leads_to: "location_1", description: "The path back to the haunted forest."}]->(l1)