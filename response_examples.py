# Example Responese for the main routes

add_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "add": {
                        "summary": "Addition Problem",
                        "value": {
                            "first": 82,
                            "second": 68,
                            "operation": "+",
                            "expression": "82 + 68",
                            "answer": 150
                        }                        
                    }
                }
            }
        }
    },
}

sub_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "sub": {
                        "summary": "Subtraction Problem",
                        "value": {
                            "first": 45,
                            "second": 8,
                            "operation": "-",
                            "expression": "45 - 8",
                            "answer": 37
                        }                        
                    }
                }
            }
        }
    },
}

mul_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "mul": {
                        "summary": "Multiplication Problem",
                        "value": {
                            "first": 11,
                            "second": 47,
                            "operation": "*",
                            "expression": "11 * 47",
                            "answer": 517
                        }                        
                    }
                }
            }
        }
    },
}

div_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "div": {
                        "summary": "Division Problem",
                        "value": {
                            "first": 36,
                            "second": 3,
                            "operation": "/",
                            "expression": "36 / 3",
                            "answer": 12
                        }                        
                    }
                }
            }
        }
    },
}

random_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "add": {
                        "summary": "Addition Problem",
                        "value": {
                            "first": 82,
                            "second": 68,
                            "operation": "+",
                            "expression": "82 + 68",
                            "answer": 150
                        }                        
                    },
                    "sub": {
                        "summary": "Subtraction Problem",
                        "value": {
                            "first": 45,
                            "second": 8,
                            "operation": "-",
                            "expression": "45 - 8",
                            "answer": 37
                        }                        
                    },
                    "mul": {
                        "summary": "Multiplication Problem",
                        "value": {
                            "first": 11,
                            "second": 47,
                            "operation": "*",
                            "expression": "11 * 47",
                            "answer": 517
                        }                        
                    },
                    "div": {
                        "summary": "Division Problem",
                        "value": {
                            "first": 36,
                            "second": 3,
                            "operation": "/",
                            "expression": "36 / 3",
                            "answer": 12
                        }                        
                    }
                    
                }
            }
        }
    },
}